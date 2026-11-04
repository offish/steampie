from .provider import Provider


class SteamSupply(Provider):
    def get_url_and_params(
        self,
        steam_id: str | int,
        app_id: int | str,
        context_id: int | str,
        cursor: str | None = None,
    ) -> tuple[str, dict]:
        del cursor
        url = f"https://steam.supply/API/{self.api_key}/loadinventory"
        params = {"steamid": str(steam_id), "appid": int(app_id), "contextid": int(context_id)}

        return url, params
