from .provider import Provider


class SteamApis(Provider):
    def get_url_and_params(
        self, steam_id: str | int, app_id: int | str, context_id: int | str, cursor: str | None = None
    ) -> tuple[str, dict]:
        url = f"https://api.steamapis.com/steam/inventory/{steam_id}/{app_id}/{context_id}"
        params = {"api_key": self.api_key}

        return url, params
