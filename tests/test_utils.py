from steampie import utils


def test_text_between() -> None:
    text = 'var a = "dupadupa";'
    text_between = utils.text_between(text, 'var a = "', '";')
    assert text_between == "dupadupa"


def test_texts_between() -> None:
    text = "<li>element 1</li>\n<li>some random element</li>"
    items = list(utils.texts_between(text, "<li>", "</li>"))
    assert items == ["element 1", "some random element"]


def test_account_id_to_steam_id() -> None:
    account_id = "293059984"
    steam_id = utils.account_id_to_steam_id(account_id)
    assert steam_id == "76561198253325712"


def test_steam_id_to_account_id() -> None:
    steam_id = "76561198253325712"
    account_id = utils.steam_id_to_account_id(steam_id)
    assert account_id == "293059984"


def test_get_key_value_from_url() -> None:
    url = "https://steamcommunity.com/tradeoffer/new/?partner=aaa&token=bbb"
    assert utils.get_key_value_from_url(url, "partner") == "aaa"
    assert utils.get_key_value_from_url(url, "token") == "bbb"


def test_get_key_value_from_url_case_insensitive() -> None:
    url = "https://steamcommunity.com/tradeoffer/new/?Partner=aaa&Token=bbb"
    assert utils.get_key_value_from_url(url, "partner", case_sensitive=False) == "aaa"
    assert utils.get_key_value_from_url(url, "token", case_sensitive=False) == "bbb"
