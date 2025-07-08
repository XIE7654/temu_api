# import pytest
import json
from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

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
    with open('order_list_g.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # print('list_orders_v2', res)
    # print('-------------')
    # res = temu_client.order.detail_order_v2(parent_order_sn='PO-211-00822146499192890')
    # print('detail_order_v2', res)
    # print('-------------')
    # res = temu_client.order.shippinginfo_order_v2(parent_order_sn='PO-211-00822146499192890')
    # print('shippinginfo_order_v2', res)
    # print('-------------')
    # res = temu_client.order.combinedshipment_list_order()
    # print('combinedshipment_list_order', res)
    # print('-------------')
    # res = temu_client.order.customization_order()
    # print('customization_order', res)
    # print('-------------')
    # res = temu_client.order.decryptshippinginfo_order(parent_order_sn='PO-211-20063653668472890')
    # print('decryptshippinginfo_order', res)
    # print('-------------')
    # assert result['status'] == 'success'

def test_order_amount_query():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    parent_order_sn = 'PO-211-00822146499192890'  # 示例父订单号
    res = temu_client.order.amount_query(parent_order_sn=parent_order_sn)
    print('amount_query', res)
    print('-------------')

if __name__ == '__main__':
    test_order_example()
    test_order_amount_query()