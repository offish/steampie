from typing import Any

from .provider import Provider


class ExpressLoad(Provider):
    def get_headers(self, steam_id: str | int | None = None) -> dict[str, Any]:
        del steam_id
        return {"X-API-Key": self.api_key, "User-Agent": "tf2-express"}

    def get_url_and_params(
        self,
        steam_id: str | int,
        app_id: int | str,
        context_id: int | str,
        cursor: str | None = None,
    ) -> tuple[str, dict]:
        del cursor
        url = f"https://api.express-load.com/inventory/{steam_id}/{app_id}/{context_id}"
        params = {}

        return url, params
