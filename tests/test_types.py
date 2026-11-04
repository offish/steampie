import json
from pathlib import Path

import pytest

from src.steampie import Asset, Description, InventoryResponse

from .utils import check_typed_dict

INVENTORIES_DIR = Path(__file__).parent / "inventories"


def load_inventories() -> dict[str, InventoryResponse]:
    return {file.stem: json.loads(file.read_text(encoding="utf-8")) for file in sorted(INVENTORIES_DIR.glob("*.json"))}


def _collect(key: str, id_key: str) -> list:
    return [
        pytest.param(entry, id=f"{entry[id_key]}-{stem}")
        for stem, inventory in load_inventories().items()
        for entry in inventory[key]
    ]


def get_inventories():
    return [pytest.param(inventory, id=stem) for stem, inventory in load_inventories().items()]


def get_assets():
    return _collect("assets", "assetid")


def get_descriptions():
    return _collect("descriptions", "market_hash_name")


@pytest.mark.parametrize("inventory", get_inventories())
def test_inventory_response(inventory: InventoryResponse):
    check_typed_dict(inventory, InventoryResponse)


@pytest.mark.parametrize("asset", get_assets())
def test_asset(asset: Asset):
    check_typed_dict(asset, Asset)


@pytest.mark.parametrize("description", get_descriptions())
def test_description(description: Description):
    check_typed_dict(description, Description)
