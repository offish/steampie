from typing import NotRequired, TypedDict


class FailedResponse(TypedDict):
    success: int
    message: str


class DescriptionValue(TypedDict):
    name: str
    value: str
    color: NotRequired[str]
    type: NotRequired[str]


class Action(TypedDict):
    name: str
    link: str


class Tag(TypedDict):
    category: str
    internal_name: str
    localized_category_name: str
    localized_tag_name: str
    color: NotRequired[str]


class Asset(TypedDict):
    appid: int
    contextid: str
    assetid: str
    classid: str
    instanceid: str
    amount: str


class Description(TypedDict):
    appid: int
    classid: str
    instanceid: str
    currency: int
    background_color: str
    icon_url: str
    icon_url_large: str
    descriptions: NotRequired[list[DescriptionValue]]
    tradable: int
    actions: list[Action]
    fraudwarnings: NotRequired[list[str]]
    name: str
    name_color: str
    type: str
    market_name: str
    market_hash_name: str
    market_actions: NotRequired[list[Action]]
    commodity: int
    market_tradable_restriction: int
    market_marketable_restriction: int
    marketable: int
    tags: list[Tag]
    sealed: int
    sealed_type: int


class Item(Asset, Description): ...


class InventoryResponse(TypedDict):
    assets: list[Asset]
    descriptions: list[Description]
    more_items: NotRequired[int]
    last_assetid: NotRequired[str]
    total_inventory_count: int
    success: int
    rwgrsn: int


class MaFileSession(TypedDict):
    SessionID: str
    steamLogin: str
    steamLoginSecure: str
    WebCookie: NotRequired[str] | None
    OAuthToken: str
    SteamID: str


class MaFile(TypedDict):
    status: int
    shared_secret: str
    serial_number: str
    revocation_code: str
    uri: str
    server_time: str
    account_name: str
    token_gid: str
    identity_secret: str
    secret_1: str
    device_id: str
    fully_enrolled: bool
    Session: MaFileSession


class MaFileSummary(TypedDict):
    steam_id: str
    username: str
    shared_secret: str
    identity_secret: str
