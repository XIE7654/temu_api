from temu_api import api
from temu_api.utils.base_client import BaseClient


class TemuClient(BaseClient):

    def __init__(self, app_key, app_secret, access_token, base_url: str, debug=False):
        super().__init__(app_key, app_secret, access_token, base_url, debug)
        self.auth = api.Auth(self)
        self.order = api.Order(self)