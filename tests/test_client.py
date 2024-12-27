import json

import pytest

from steampie.client import SteamClient
from steampie.exceptions import LoginRequired
from steampie.models import Asset, GameOptions


def test_steam_login(client) -> None:
    assert client.is_session_alive()


def test_get_steam_id(client, credentials) -> None:
    steam_guard_file = json.loads(credentials["steam_guard_file"])

    assert client.get_steam_id() == int(steam_guard_file["Session"]["SteamID"])


def test_sessionid_cookie(client) -> None:
    community_cookies = client._session.cookies.get_dict("steamcommunity.com")
    store_cookies = client._session.cookies.get_dict("store.steampowered.com")

    assert "sessionid" in community_cookies
    assert "sessionid" in store_cookies


def test_get_my_inventory(client) -> None:
    inventory = client.get_my_inventory(GameOptions.CS)
    assert inventory is not None


def test_get_partner_inventory(client) -> None:
    partner_id = "76561198449257208"
    game = GameOptions.TF2
    inventory = client.get_partner_inventory(partner_id, game)
    assert inventory is not None


def test_get_trade_offers_summary(client) -> None:
    summary = client.get_trade_offers_summary()
    assert summary is not None


def test_get_trade_offers(client) -> None:
    offers = client.get_trade_offers()
    assert offers is not None


# def test_get_trade_offer() -> None:
#     trade_offer_id = "488991480"
#     offer = client.get_trade_offer(trade_offer_id)
#     assert offer is not None


# def test_accept_trade_offer() -> None:
#     trade_offer_id = "1451378159"
#     response_dict = client.accept_trade_offer(trade_offer_id)
#     assert response_dict is not None


# def test_decline_trade_offer() -> None:
#     trade_offer_id = "1449530707"
#     response_dict = client.decline_trade_offer(trade_offer_id)
#     assert response_dict["response"] == {}


# def test_cancel_trade_offer() -> None:
#     trade_offer_id = "1450637835"
#     response_dict = client.cancel_trade_offer(trade_offer_id)
#     assert response_dict["response"] == {}


def test_make_offer(client) -> None:
    partner_id = "488991480"
    game = GameOptions.TF2
    my_items = client.get_my_inventory(game)
    partner_items = client.get_partner_inventory(partner_id, game)
    my_first_item = next(iter(my_items.values()))
    partner_first_item = next(iter(partner_items.values()))
    my_asset = Asset(my_first_item["id"], game)
    partner_asset = Asset(partner_first_item["id"], game)
    response = client.make_offer([my_asset], [partner_asset], partner_id, "test offer")

    assert response is not None
    assert "tradeofferid" in response


# def test_make_offer_url() -> None:
#     partner_account_id = "488991480"
#     partner_token = "7vqRtBpC"
#     sample_trade_url = f"https://steamcommunity.com/tradeoffer/new/?partner={partner_account_id}&token={partner_token}"
#     client = SteamClient(self.credentials.api_key)
#     client.login(
#         self.credentials.login, self.credentials.password, self.steam_guard_file
#     )
#     client._session.request("HEAD", "http://steamcommunity.com")
#     partner_steam_id = account_id_to_steam_id(partner_account_id)
#     game = GameOptions.CS
#     my_items = client.get_my_inventory(game, merge=False)["rgInventory"]
#     partner_items = client.get_partner_inventory(partner_steam_id, game, merge=False)[
#         "rgInventory"
#     ]
#     my_first_item = next(iter(my_items.values()))
#     partner_first_item = next(iter(partner_items.values()))
#     my_asset = Asset(my_first_item["id"], game)
#     partner_asset = Asset(partner_first_item["id"], game)
#     response = client.make_offer_with_url(
#         [my_asset], [partner_asset], sample_trade_url, "TESTOWA OFERTA"
#     )

#     assert response is not None
#     assert "tradeofferid" in response


def test_get_escrow_duration(client) -> None:
    # A sample trade URL with escrow time of 15 days cause mobile auth not added
    sample_trade_url = (
        "https://steamcommunity.com/tradeoffer/new/?partner=314218906&token=sgA4FdNm"
    )
    response = client.get_escrow_duration(sample_trade_url)
    assert response == 15


def test_logout(client) -> None:
    assert client.is_session_alive()
    client.logout()
    assert not client.is_session_alive()


def test_send_offer_without_sessionid_cookie(credentials: dict) -> None:
    client = SteamClient(credentials["api_key"])
    client.login(
        credentials["username"],
        credentials["password"],
        credentials["steam_guard_file"],
    )
    client._session.cookies.set("sessionid", None, domain="steamcommunity.com")
    cookies = client._session.cookies.get_dict("steamcommunity.com")
    assert "sessionid" not in cookies
    game = GameOptions.TF2
    asset_id = ""
    my_asset = Asset(asset_id, game)
    trade_offer_url = ""

    with pytest.raises(AttributeError):
        client.make_offer_with_url([my_asset], [], trade_offer_url, "TEST")


def test_accept_trade_offer_without_login(credentials: dict) -> None:
    client = SteamClient(credentials["api_key"])

    with pytest.raises(LoginRequired):
        client.accept_trade_offer("id")