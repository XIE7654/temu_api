from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

def test_delete_goods():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    goods_id = 123456789  # 示例商品ID
    res = temu_client.product.delete_goods(goods_id=goods_id)
    print('delete_goods', res)
    print('-------------')

def test_sku_list_retrieve():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    res = temu_client.product.sku_list_retrieve(
        sku_search_type="ACTIVE",  # SKU状态筛选，必填
        page_size=10,
        order_field="create_time",
        order_type=0,
        goods_id_list=[123456789],
        goods_name="测试商品"
    )
    print('sku_list_retrieve', res)
    print('-------------')

def test_goods_list_retrieve():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    res = temu_client.product.goods_list_retrieve(
        goods_search_type="ACTIVE",  # 商品状态筛选，必填
        page_size=10,
        order_field="create_time",
        order_type=0,
        goods_id_list=[123456789],
        goods_name="测试商品"
    )
    print('goods_list_retrieve', res)
    print('-------------')

def test_compliance_info_fill_list_query():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    res = temu_client.product.compliance_info_fill_list_query(
        page=1,
        size=10,
        compliance_info_type=4,  # 4:A/S负责人
        language="zh-CN",
        search_text="负责人"
    )
    print('compliance_info_fill_list_query', res)
    print('-------------')

if __name__ == '__main__':
    test_delete_goods()
    test_sku_list_retrieve()
    test_goods_list_retrieve()
    test_compliance_info_fill_list_query() 