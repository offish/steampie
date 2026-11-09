from .steam_id import account_id_to_steam_id


def has_token_in_trade_url(trade_url: str) -> bool:
    return "&token=" in trade_url


def get_account_id_from_trade_url(trade_url: str) -> str:
    partner_index = trade_url.index("?partner=") + 9
    token_index = None

    if has_token_in_trade_url(trade_url):
        token_index = trade_url.index("&token=")

    return trade_url[partner_index:token_index]


def get_steam_id_from_trade_url(trade_url: str) -> str:
    account_id = get_account_id_from_trade_url(trade_url)
    return account_id_to_steam_id(account_id)


def get_token_from_trade_url(trade_url: str) -> str | None:
    if has_token_in_trade_url(trade_url):
        token_index = trade_url.index("&token=") + 7
        return trade_url[token_index:]
