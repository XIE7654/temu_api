from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Auth(BaseAPI):

    @action("bg.open.accesstoken.info.get")
    def get_access_token_info(self, **kwargs) -> ApiResponse:
        """
        This interface allows merchants to view the API permissions associated with their currently authorized token,
         providing a list of authorized API endpoints.
        """
        return self._request(data={**kwargs})

    @action("bg.open.accesstoken.create")
    def create_access_token_info(self, **kwargs) -> ApiResponse:
        """
        Temu's authorization callback interface allows developers to receive notifications when a
        user has successfully authorized their application. When after the user grants permission,
        Temu will redirect back to the developer's specified callback URL with an authorization code.
        Use this api to request an access token.
        """
        return self._request(data={**kwargs})