import hashlib

import logging
import time

import requests
from .api_response import ApiResponse
from .helpers import filter_none

log = logging.getLogger(__name__)


class BaseClient(object):
    method = 'GET'

    def __init__(self, app_key, app_secret, access_token, base_url: str, debug = False):
        self.app_key = app_key
        self.app_secret = app_secret
        self.access_token = access_token
        self.base_url = base_url
        self.debug = debug
        self.headers = {
            "content-type": "application/json;charset=UTF-8",
        }
        self.common_params = {
            "app_key": self.app_key,
            "access_token": self.access_token,
            "data_type": "JSON",
        }

    def _md5(self, text: str) -> str:
        """计算输入字符串的 MD5 哈希值"""
        md5_hash = hashlib.md5(text.encode('utf-8'))  # 计算 MD5
        return md5_hash.hexdigest().upper()  # 返回十六进制字符串

    def _get_sign(self, params):
        sorted_params = dict(sorted(params.items()))
        # 字符串连接 $key 和 $value
        result_str = ''.join([f"{key}{value}" for key, value in sorted_params.items()])
        result_str = result_str.replace(" ", "").replace("'", '"')
        concatenated_str = f'{self.app_secret}{result_str}{self.app_secret}'
        sign = self._md5(concatenated_str)
        return sign

    def _api_url(self):
        return self.base_url + '/openapi/router'

    def _params(self, api_type, extra_params={}):
        params = {
            'type': api_type,
            'app_key': self.app_key,
            'access_token': self.access_token,
            'timestamp': round(time.time()),
            "data_type": "JSON",
        }
        if extra_params:
            filtered_params = filter_none(extra_params)
            params.update(filtered_params)
        sign = self._get_sign(params)
        params['sign'] = sign
        return params

    def request(self, data: dict = None) -> ApiResponse:
        api_type = data.pop('path')
        method = data.pop('method')
        data = self._params(api_type, data)
        if method.upper() == "GET":
            response = requests.get(url=self._api_url(), headers=self.headers, params=data)
        else:
            response = requests.post(url=self._api_url(), headers=self.headers, json=data)
        return response.json()
    