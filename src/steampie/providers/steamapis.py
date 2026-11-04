from .provider import Provider


class SteamApis(Provider):
    def get_headers(self, steam_id: str | None = None) -> dict[str, str]:
        del steam_id
        return {"x-api-key": self.api_key}

    def get_url_and_params(
        self,
        steam_id: str | int,
        app_id: int | str,
        context_id: int | str,
        cursor: str | None = None,
    ) -> tuple[str, dict]:
        del cursor

        url = f"https://api.steamapis.com/v2/steam/users/{steam_id}/inventory/{app_id}/{context_id}"
        params = {}

        return url, params
