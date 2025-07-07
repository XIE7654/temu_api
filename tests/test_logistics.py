import json
from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

def test_logistics_example():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)

    # 获取仓库信息
    res = temu_client.logistics.warehouse_list()
    print('warehouse_list', res)
    print('-------------')

    # 获取区域物流公司
    res = temu_client.logistics.companies(region_id=211)
    print('companies', res)
    print('-------------')

    # 查询包裹支持的物流服务商
    res = temu_client.logistics.shipping_services(
        warehouse_id='WH-05022784921732414',
        order_sn_list=['211-00822146499192890', '211-20357915551350400', '211-20129665582713264', '211-20129770440313264'],
        weight='2',  # 整数部分
        weight_unit='lb',
        length='3.94',
        width='3.94',
        height='3.94',
        dimension_unit='in'
    )
    print('shipping_services', res)
    print('-------------')

    # 获取所有在线发货物流类型
    res = temu_client.logistics.ship_logistics_type(region_id=211)
    print('ship_logistics_type', res)
    print('-------------')

if __name__ == '__main__':
    test_logistics_example() 