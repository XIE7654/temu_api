# import pytest

from temu_api import TemuClient

APP_KEY = '4ebbc9190ae410443d65b4c2faca981f'
APP_SECRET = '4782d2d827276688bf4758bed55dbdd4bbe79a79'
ACCESS_TOKEN = 'uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7'
BASE_URL = 'https://openapi-b-us.temu.com'
def test_auth_example():
    # 示例：假设有一个 login 方法
    # result = auth.login('username', 'password')
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    res = temu_client.auth.get_access_token_info()
    print(res)
    print('-------------')
    res = temu_client.auth.create_access_token_info()
    print(res)
    # assert result['status'] == 'success'

if __name__ == '__main__':
    test_auth_example()