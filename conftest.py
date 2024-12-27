import json
from base64 import b64encode

import pytest

from steampie.client import SteamClient


@pytest.fixture
def shared_secret() -> bytes:
    return b64encode(b"1234567890abcdefghij")


@pytest.fixture
def identity_secret() -> bytes:
    return b64encode(b"abcdefghijklmnoprstu")


def get_credentials() -> dict:
    steam_credentials = {}

    with open("./credentials.json", "r") as f:
        steam_credentials = json.load(f)

    return steam_credentials


@pytest.fixture
def credentials() -> dict:
    return get_credentials()


@pytest.fixture
def steam_guard_file() -> dict:
    steam_guard_credentials = {}

    with open("./76561198253325712.maFile", "r") as f:
        steam_guard_credentials = json.load(f)

    steam_credentials = get_credentials()

    steam_guard_credentials["password"] = steam_credentials["password"]
    steam_guard_credentials["api_key"] = steam_credentials["api_key"]

    return steam_guard_credentials


steam_credentials = get_credentials()
steam_client = SteamClient(**steam_credentials)
steam_client.login()


@pytest.fixture
def client() -> SteamClient:
    return steam_client
