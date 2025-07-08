from temu_api import api
from temu_api.utils.base_client import BaseClient


class TemuClient(BaseClient):

    def __init__(self, app_key: str, app_secret: str, access_token: str, base_url: str, debug=False):
        super().__init__(app_key, app_secret, access_token, base_url, debug)
        self.auth = api.Auth(self)
        self.ads = api.Ads(self)
        self.aftersales = api.Aftersales(self)
        self.order = api.Order(self)
        self.logistics = api.Logistics(self)
        self.promotion = api.Promotion(self)
        self.price = api.Price(self)
        self.product = api.Product(self)
        self.fulfillment = api.Fulfillment(self)