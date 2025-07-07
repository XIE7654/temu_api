from temu_api import TemuClient
from conftest import APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL

def test_aftersales_example():
    temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)

    # 查询父售后单列表
    # res = temu_client.aftersales.parent_aftersales_list(parent_order_sn_list=['PO-128-01453433636470441'])
    # print('parent_aftersales_list', res)
    # print('-------------')

    # # 查询售后服务请求列表（需传 parent_after_sales_sn_list）
    res = temu_client.aftersales.aftersales_list(parent_after_sales_sn_list=['PO-128-01453433636470441'])
    print('aftersales_list', res)
    print('-------------')
    #
    # # 查询父售后单详情
    # res = temu_client.aftersales.parent_aftersales_detail(parent_order_sn='your_parent_order_sn', parent_after_sales_sn='your_parent_after_sales_sn')
    # print('parent_aftersales_detail', res)
    # print('-------------')
    #
    # # 售后退款处理
    # res = temu_client.aftersales.refund_issue(parent_after_sales_sn='your_parent_after_sales_sn', parent_order_sn='your_parent_order_sn', open_api_refund_type=1)
    # print('refund_issue', res)
    # print('-------------')
    #
    # # 查询父售后单退货物流信息
    # res = temu_client.aftersales.parent_return_order(parent_after_sales_sn='your_parent_after_sales_sn')
    # print('parent_return_order', res)
    # print('-------------')

if __name__ == '__main__':
    test_aftersales_example() 