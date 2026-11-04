from .provider import Provider


class SteamCommunity(Provider):
    def get_headers(self, steam_id: str | int | None = None) -> dict[str, str]:
        return {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/avif,image/webp,image/apng,*/*;q=0.8,"
                "application/signed-exchange;v=b3;q=0.7"
            ),
            "Accept-Language": "en-US,en;q=0.9,ja;q=0.8,ms;q=0.7",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Referer": f"https://steamcommunity.com/profiles/{steam_id}/inventory",
        }

    def get_url_and_params(
        self, steam_id: str | int, app_id: int | str, context_id: int | str, cursor: str | None = None
    ) -> tuple[str, dict[str, str | int]]:
        url = f"https://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}"
        params: dict[str, str | int] = {"l": "english", "count": 2500}

        if cursor is not None:
            params["start_assetid"] = cursor

        return url, params
