# import pytest
import json

from temu_api import TemuClient

APP_KEY = '4ebbc9190ae410443d65b4c2faca981f'
APP_SECRET = '4782d2d827276688bf4758bed55dbdd4bbe79a79'
ACCESS_TOKEN = 'uplv3hfyt5kcwoymrgnajnbl1ow5qxlz4sqhev6hl3xosz5dejrtyl2jre7'
BASE_URL = 'https://openapi-b-us.temu.com'
def test_order_example():
    # 示例：假设有一个 login 方法
    # result = auth.login('username', 'password')
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    res = temu_client.order.list_orders_v2()
    if hasattr(res, 'to_dict'):
        data = res.to_dict()
    elif hasattr(res, '__dict__'):
        data = res.__dict__
    else:
        data = res
    with open('order_list.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('list_orders_v2', res)
    print('-------------')
    res = temu_client.order.detail_order_v2(parent_order_sn='PO-211-00822146499192890')
    print('detail_order_v2', res)
    print('-------------')
    res = temu_client.order.shippinginfo_order_v2(parent_order_sn='PO-211-00822146499192890')
    print('shippinginfo_order_v2', res)
    print('-------------')
    res = temu_client.order.combinedshipment_list_order()
    print('combinedshipment_list_order', res)
    print('-------------')
    res = temu_client.order.customization_order()
    print('customization_order', res)
    print('-------------')
    res = temu_client.order.decryptshippinginfo_order(parent_order_sn='PO-211-20063653668472890')
    print('decryptshippinginfo_order', res)
    print('-------------')
    # assert result['status'] == 'success'

if __name__ == '__main__':
    test_order_example()