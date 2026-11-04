from .provider import Provider


class Custom(Provider):
    def __init__(self, api_key: str, url: str) -> None:
        super().__init__(api_key)
        self.url = url.removesuffix("/")

    def get_url_and_params(
        self,
        steam_id: str | int,
        app_id: int | str,
        context_id: int | str,
        cursor: str | None = None,
    ) -> tuple[str, dict]:
        del cursor
        url = f"{self.url}/inventory/{steam_id}/{app_id}/{context_id}"
        params = {}

        if self.api_key:
            params = {"api_key": self.api_key}

        return url, params
