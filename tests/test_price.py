from pprint import pprint
from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

def test_priceorder_negotiate():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
    # 议价接口参数示例
    price_order_id = 1234567890  # 定价单ID
    negotiated_price_sku_list = [
        {
            "skuId": 111111,
            "negotiatedPrice": 99.99,
            "reason": "Test negotiation"
        }
    ]
    goods_id = 2222222  # 商品ID
    price_commit_version = 1  # 价格提交版本
    price_commit_id = 3333333  # 价格提交ID
    external_link_list = ["https://example.com/info1", "https://example.com/info2"]
    # 调用议价接口
    res = temu_client.price.priceorder_negotiate(
        price_order_id=price_order_id,
        negotiated_price_sku_list=negotiated_price_sku_list,
        goods_id=goods_id,
        price_commit_version=price_commit_version,
        price_commit_id=price_commit_id,
        external_link_list=external_link_list
    )
    print('priceorder_negotiate', res)
    print('-------------')

if __name__ == '__main__':
    test_priceorder_negotiate() 