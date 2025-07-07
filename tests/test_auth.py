# import pytest

from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

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