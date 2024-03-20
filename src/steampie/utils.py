import os
import copy
import struct
from typing import List
from urllib.parse import urlparse, parse_qs

import requests
from requests.structures import CaseInsensitiveDict

from .models import GameOptions
from .exceptions import ProxyConnectionError, LoginRequired


def login_required(func):
    def func_wrapper(self, *args, **kwargs):
        if not self.was_login_executed:
            raise LoginRequired("Use login method first")
        else:
            return func(self, *args, **kwargs)

    return func_wrapper


def text_between(text: str, begin: str, end: str) -> str:
    start = text.index(begin) + len(begin)
    end = text.index(end, start)
    return text[start:end]


def texts_between(text: str, begin: str, end: str):
    stop = 0
    while True:
        try:
            start = text.index(begin, stop) + len(begin)
            stop = text.index(end, start)
            yield text[start:stop]
        except ValueError:
            return


def account_id_to_steam_id(account_id: str | int) -> str:
    """Convert AccountID to SteamID.

    Args:
        account_id: AccountID

    Returns:
        SteamID64 as a string
    """
    first_bytes = int(account_id).to_bytes(4, byteorder="big")
    last_bytes = 0x1100001.to_bytes(4, byteorder="big")
    return str(struct.unpack(">Q", last_bytes + first_bytes)[0])


def steam_id_to_account_id(steam_id: str | int) -> str:
    """Convert SteamID to AccountID.

    Args:
        steam_id: SteamID64

    Returns:
        AccountID as a string
    """
    return str(struct.unpack(">L", int(steam_id).to_bytes(8, byteorder="big")[4:])[0])


def merge_items_with_descriptions_from_inventory(
    inventory_response: dict, game: GameOptions
) -> dict:
    """Merge items with their descriptions from the inventory response.

    Args:
        inventory_response: Inventory response from Steam API
        game: GameOptions enum

    Returns:
        Merged items with their descriptions
    """
    inventory = inventory_response.get("assets", [])
    if not inventory:
        return {}
    descriptions = {
        get_description_key(description): description
        for description in inventory_response["descriptions"]
    }
    return merge_items(inventory, descriptions, context_id=game.context_id)


def merge_items_with_descriptions_from_offers(offers_response: dict) -> dict:
    """Merge items with their descriptions from the offers response.

    Args:
        offers_response: Offers response from Steam API

    Returns:
        Merged items with their descriptions
    """
    descriptions = {
        get_description_key(offer): offer
        for offer in offers_response["response"].get("descriptions", [])
    }
    received_offers = offers_response["response"].get("trade_offers_received", [])
    sent_offers = offers_response["response"].get("trade_offers_sent", [])
    offers_response["response"]["trade_offers_received"] = list(
        map(
            lambda offer: merge_items_with_descriptions_from_offer(offer, descriptions),
            received_offers,
        )
    )
    offers_response["response"]["trade_offers_sent"] = list(
        map(
            lambda offer: merge_items_with_descriptions_from_offer(offer, descriptions),
            sent_offers,
        )
    )
    return offers_response


def merge_items_with_descriptions_from_offer(offer: dict, descriptions: dict) -> dict:
    """Merge items with their descriptions from the offer.

    Args:
        offer: Offer dictionary
        descriptions: Descriptions dictionary

    Returns:
        Merged offer
    """
    merged_items_to_give = merge_items(offer.get("items_to_give", []), descriptions)
    merged_items_to_receive = merge_items(
        offer.get("items_to_receive", []), descriptions
    )
    offer["items_to_give"] = merged_items_to_give
    offer["items_to_receive"] = merged_items_to_receive
    return offer


def merge_items_with_descriptions_from_listing(
    listings: dict, ids_to_assets_address: dict, descriptions: dict
) -> dict:
    """Merge items with their descriptions from the listing.

    Args:
        listings: Listings dictionary
        ids_to_assets_address: IDs to assets address dictionary
        descriptions: Descriptions dictionary

    Returns:
        Merged listings
    """
    for listing_id, listing in listings.get("sell_listings").items():
        asset_address = ids_to_assets_address[listing_id]
        description = descriptions[asset_address[0]][asset_address[1]][asset_address[2]]
        listing["description"] = description
    return listings


def merge_items(items: List[dict], descriptions: dict, **kwargs) -> dict:
    """Merge items with their descriptions.

    Args:
        items: List of items
        descriptions: Descriptions dictionary
        kwargs: Additional keyword arguments

    Returns:
        Merged items
    """
    merged_items = {}

    for item in items:
        description_key = get_description_key(item)
        description = copy.copy(descriptions[description_key])
        item_id = item.get("id") or item["assetid"]
        description["contextid"] = item.get("contextid") or kwargs["context_id"]
        description["id"] = item_id
        description["amount"] = item["amount"]
        merged_items[item_id] = description

    return merged_items


def get_description_key(item: dict) -> str:
    return f'{item["classid"]}_{item["instanceid"]}'


def get_key_value_from_url(url: str, key: str, case_sensitive: bool = True) -> str:
    params = urlparse(url).query
    return (
        parse_qs(params)[key][0]
        if case_sensitive
        else CaseInsensitiveDict(parse_qs(params))[key][0]
    )


def load_credentials():
    dirname = os.path.dirname(os.path.abspath(__file__))
    with open(f"{dirname}/../secrets/credentials.pwd", "r") as f:
        return [
            Credentials(line.split()[0], line.split()[1], line.split()[2]) for line in f
        ]


class Credentials:
    def __init__(self, login: str, password: str, api_key: str):
        self.login = login
        self.password = password
        self.api_key = api_key


def ping_proxy(proxies: dict):
    try:
        requests.get("https://steamcommunity.com/", proxies=proxies)
        return True
    except Exception:
        raise ProxyConnectionError("Proxy not working for steamcommunity.com")


def create_cookie(name: str, cookie: str, domain: str) -> dict:
    return {"name": name, "value": cookie, "domain": domain}
