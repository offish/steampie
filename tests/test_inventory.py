from aiohttp import ClientSession

from src.steampie import AsyncInventory, Inventory


def test_default_inventory_provider() -> None:
    inventory = Inventory()
    assert inventory.provider.__class__.__name__ == "SteamCommunity"
    assert inventory.provider.api_key == ""


def test_steamcommunity_inventory_provider() -> None:
    inventory = Inventory("steamcommunity", "api_key")
    assert inventory.provider.__class__.__name__ == "SteamCommunity"
    assert inventory.provider.api_key == "api_key"


def test_express_load_inventory_provider() -> None:
    inventory = Inventory("expressload", "api_key")
    assert inventory.provider.__class__.__name__ == "ExpressLoad"
    assert inventory.provider.api_key == "api_key"


def test_steamsupply_inventory_provider() -> None:
    inventory = Inventory("steamsupply", "api_key")
    assert inventory.provider.__class__.__name__ == "SteamSupply"
    assert inventory.provider.api_key == "api_key"


def test_custom_inventory_provider() -> None:
    inventory = Inventory("http://example.com", "api_key")
    assert inventory.provider.__class__.__name__ == "Custom"
    assert inventory.provider.api_key == "api_key"


def test_steamapis_inventory_provider() -> None:
    inventory = Inventory("steamapis", "api_key")
    assert inventory.provider.__class__.__name__ == "SteamApis"
    assert inventory.provider.api_key == "api_key"


def test_invalid_express_load_inventory_fetch() -> None:
    provider = Inventory("expressload", "abc123")
    response = provider.fetch(76561198253325712)

    assert not response["success"]
    assert "invalid_api_key" in response["message"]


def test_steam_community_inventory_fetch() -> None:
    provider = Inventory("steamcommunity")
    response = provider.fetch("76561198253325712", "440", "2")

    assert response.get("success")
    assert response.get("assets")
    assert response.get("descriptions")


async def test_async_steam_community_fetch() -> None:
    session = ClientSession()
    provider = AsyncInventory(session)
    response = await provider.fetch("76561198253325712", "440", "2")

    assert response.get("success")
    assert response.get("assets")
    assert response.get("descriptions")
