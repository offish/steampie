from steampie import guard
from steampie.confirmation import Tag


def test_one_time_code(shared_secret) -> None:
    timestamp = 1469184207
    code = guard.generate_one_time_code(shared_secret, timestamp)
    assert code == "P2QJN"


def test_confirmation_key(identity_secret) -> None:
    timestamp = 1470838334
    confirmation_key = guard.generate_confirmation_key(
        identity_secret, Tag.CONF.value, timestamp
    )
    assert confirmation_key == b"pWqjnkcwqni+t/n+5xXaEa0SGeA="


def test_generate_device_id() -> None:
    steam_id = "12341234123412345"
    device_id = guard.generate_device_id(steam_id)
    assert device_id == "android:677cf5aa-3300-7807-d1e2-c408142742e2"


def test_load_steam_guard() -> None:
    guard_json_str = '{"steamid": 12345678, "shared_secret": "SHARED_SECRET", "identity_secret": "IDENTITY_SECRET"}'
    guard_data = guard.load_steam_guard(guard_json_str)

    for key in ["steamid", "shared_secret", "identity_secret"]:
        assert key in guard_data
        assert isinstance(guard_data[key], str)
