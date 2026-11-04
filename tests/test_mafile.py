from pathlib import Path
from typing import NamedTuple

import pytest

from src.steampie import get_mafile_data, is_mafile_unencrypted
from src.steampie.mafile import has_manifest_file

MAFILES_PATH = Path(__file__).parent / "maFiles"

HAS_MANIFEST = {
    "76561199023865941.maFile": False,
    "76561199024057705.maFile": False,
    "76561199024144425.maFile": False,
    "76561199023863151.maFile": True,
    "lymphangiomata.maFile": False,
}


IS_UNENCRYPTED = {
    "76561199023865941.maFile": True,
    "76561199024057705.maFile": True,
    "76561199024144425.maFile": True,
    "76561199023863151.maFile": False,
    "lymphangiomata.maFile": True,
}


class Expected(NamedTuple):
    steam_id: str
    username: str
    identity_secret: str
    shared_secret: str
    passphrase: str | None = None


MAFILE_DATA = {
    "76561199023865941.maFile": Expected(
        steam_id="76561199023865941",
        username="agglutinogenic",
        identity_secret="wiYRwKkTHobdDdSgppGbePf8aso=",
        shared_secret="LdDvyCO6bbyVXteuop6s6wFl0Zo=",
    ),
    "76561199024057705.maFile": Expected(
        steam_id="76561199024057705",
        username="antidiphtheritic",
        identity_secret="3v3PdEhFz28eKouF8851epvKeX8=",
        shared_secret="YI0+x8tPHnDrmG63U11wPQDiChg=",
    ),
    "76561199024144425.maFile": Expected(
        steam_id="76561199024144425",
        username="carbonylate",
        identity_secret="ixIYCwde3Jl3Q29uY1mo2wxxJsw=",
        shared_secret="56VVJyz40M9fHxSAoj2VvH5AetA=",
    ),
    "76561199023863151.maFile": Expected(
        steam_id="76561199023863151",
        username="consumingly",
        identity_secret="+q57VyyNkQ32PBSUl86lmX88Mrk=",
        shared_secret="ejJG39uG9e95npjnJS2W7TzumVY=",
        passphrase="1111",
    ),
    "lymphangiomata.maFile": Expected(
        steam_id="76561199023625595",
        username="lymphangiomata",
        identity_secret="rIWzJz2IjXeBU51+xxfo5PvxxN4=",
        shared_secret="ps4Bshn4FBO2yLYGPlw+C49NTRE=",
    ),
}


@pytest.mark.parametrize("file_name, expected", HAS_MANIFEST.items(), ids=list(HAS_MANIFEST))
def test_has_manifest_file(file_name: str, expected: bool):
    assert has_manifest_file(MAFILES_PATH / file_name) is expected


@pytest.mark.parametrize("file_name, expected", IS_UNENCRYPTED.items(), ids=list(IS_UNENCRYPTED))
def test_is_mafile_unencrypted(file_name: str, expected: bool):
    assert is_mafile_unencrypted(MAFILES_PATH / file_name) is expected


@pytest.mark.parametrize("file_name, expected", MAFILE_DATA.items(), ids=list(MAFILE_DATA))
def test_get_mafile_data(file_name: str, expected: Expected):
    result = get_mafile_data(MAFILES_PATH / file_name, expected.passphrase)

    assert isinstance(result, dict)
    assert result["steam_id"] == expected.steam_id
    assert result["username"] == expected.username
    assert result["identity_secret"] == expected.identity_secret
    assert result["shared_secret"] == expected.shared_secret
