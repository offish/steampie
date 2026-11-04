import requests
from aiohttp import ClientSession

from .providers import PROVIDERS, Custom, Provider, SteamCommunity
from .types import FailedResponse, InventoryResponse


class Inventory:
    def __init__(self, provider_name: str = "steamcommunity", api_key: str | None = None) -> None:
        self.provider = self._get_provider(provider_name, api_key)

    def _get_provider(self, provider_name: str, api_key: str) -> Provider:
        # default to steam if no api_key is given
        if not api_key:
            return SteamCommunity()

        provider_name = provider_name.lower()

        # if provider_name is a url, assign it as a custom provider address
        if provider_name.startswith("http"):
            return Custom(api_key, provider_name)

        # loop through providers create object
        for provider in PROVIDERS:
            if provider.__name__.lower() == provider_name:
                # set the first found provider and then stop
                return provider(api_key)

    def fetch(
        self, steam_id: int | str, app_id: int | str = 440, context_id: int | str = 2, cursor: str | None = None
    ) -> InventoryResponse | FailedResponse:

        url, params = self.provider.get_url_and_params(steam_id, app_id, context_id, cursor)
        headers = self.provider.get_headers(steam_id)
        response = requests.get(url, params=params, headers=headers)

        if response.ok:
            return response.json()

        return {"success": False, "message": response.text}


class AsyncInventory(Inventory):
    def __init__(
        self,
        session: ClientSession,
        provider_name: str = "steamcommunity",
        api_key: str | None = None,
    ) -> None:
        self.session = session
        self.provider = self._get_provider(provider_name, api_key)

    async def fetch(
        self, steam_id: int | str, app_id: int | str = 440, context_id: int | str = 2, cursor: str | None = None
    ) -> InventoryResponse | FailedResponse:

        url, params = self.provider.get_url_and_params(steam_id, app_id, context_id, cursor)
        headers = self.provider.get_headers(steam_id)

        async with self.session.get(url, params=params, headers=headers) as resp:
            if not resp.ok:
                return {"success": False, "message": await resp.text()}

            return await resp.json()
