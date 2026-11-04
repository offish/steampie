from abc import ABC, abstractmethod
from typing import Any


class Provider(ABC):
    def __init__(self, api_key: str = "") -> None:
        self.api_key = api_key

    def get_headers(self, steam_id: str | int | None = None) -> dict[str, Any]:
        del steam_id
        return {}

    @abstractmethod
    def get_url_and_params(
        self,
        steam_id: str | int,
        app_id: int | str,
        context_id: int | str,
        cursor: str | None = None,
    ) -> tuple[str, dict]:
        pass
