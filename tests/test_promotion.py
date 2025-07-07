from pprint import pprint

from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

def test_promotion_example():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)

    # 查询本地活动列表
    # res = temu_client.promotion.activity_query(page_number=1, page_size=10, activity_type=2)
    # pprint('activity_query')
    # pprint(res)
    # pprint('-------------')
    # 1100000022254
    # 1100000021606
    # 1100000021192
    # 1100000022644
    activity_id = 1100000022644
    # # 查询本地活动候选商品列表
    # res = temu_client.promotion.activity_candidate_goods_query(activity_id=1100000021192, page_number=1, page_size=10)
    # print('activity_candidate_goods_query', res)
    # print('-------------')

    # 查询本地活动商品列表
    # res = temu_client.promotion.activity_goods_query(activity_id=activity_id, page_number=1, page_size=10)
    # print('activity_goods_query', res)
    # print('-------------')
    # #
    # # 报名本地活动商品
    enroll_goods = {
        "goodsId": 123456,  # 商品ID
        "enrollSkuList": [
            {
                "skuId": 654321,  # SKU ID
                "activitySupplierPrice": 100,  # 活动底价
                "activityQuantity": 10         # 活动数量
            },
            # 可以有多个SKU
            ]
    # 还可以加 traceCode 等其它参数
    }
    res = temu_client.promotion.activity_goods_enroll(activity_id=activity_id, enroll_goods=enroll_goods)
    print('activity_goods_enroll', res)
    print('-------------')

    # 查询本地活动商品操作结果
    # res = temu_client.promotion.activity_goods_operation_query(draft_id_list=[111, 222])
    # print('activity_goods_operation_query', res)
    # print('-------------')
    # #
    # # 更新本地活动商品信息
    # res = temu_client.promotion.activity_goods_update(
    #     activity_id=123456,
    #     goods_id=654321,
    #     operate_type=20,
    #     activity_quantity=100
    # )
    # print('activity_goods_update', res)
    # print('-------------')

if __name__ == '__main__':
    test_promotion_example() 