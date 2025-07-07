from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Aftersales(BaseAPI):
    @action("bg.aftersales.parentaftersales.list.get")
    def parent_aftersales_list(
        self,
        page_size: int = 10,
        page_no: int = 1,
        parent_order_sn_list: list = None,
        parent_after_sales_sn_list: list = None,
        create_at_start: int = None,
        create_at_end: int = None,
        update_at_start: int = None,
        update_at_end: int = None,
        after_sales_status_group: int = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询父售后单列表（bg.aftersales.parentaftersales.list.get）。
        :param page_size: 分页大小，默认10，最大200
        :param page_no: 分页页码，默认1
        :param parent_order_sn_list: 父订单号列表，选填
        :param parent_after_sales_sn_list: 父售后单号列表，选填
        :param create_at_start: 创建时间起始（秒），选填
        :param create_at_end: 创建时间结束（秒），选填
        :param update_at_start: 状态变更时间起始（秒），选填
        :param update_at_end: 状态变更时间结束（秒），选填
        :param after_sales_status_group: 售后单状态组，选填
        其余参数通过 kwargs 传递。
        This interface provides real-time updates on the current after-sales status of an order.
        """
        data = {
            "pageSize": page_size,
            "pageNo": page_no,
            "parentOrderSnList": parent_order_sn_list,
            "parentAfterSalesSnList": parent_after_sales_sn_list,
            "createAtStart": create_at_start,
            "createAtEnd": create_at_end,
            "updateAtStart": update_at_start,
            "updateAtEnd": update_at_end,
            "afterSalesStatusGroup": after_sales_status_group,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.aftersales.aftersales.list.get")
    def aftersales_list(
        self,
        parent_after_sales_sn_list: list,
        page_no: int = 1,
        page_size: int = 10,
        **kwargs
    ) -> ApiResponse:
        """
        查询售后服务请求列表（bg.aftersales.aftersales.list.get）。
        :param parent_after_sales_sn_list: 父售后单号列表，必填
        :param page_no: 分页页码，默认1
        :param page_size: 分页大小，默认10，最大200
        其余参数通过 kwargs 传递。
        This interface allows merchants to retrieve a list of after-sales service requests made by buyers.
        """
        data = {
            "parentAfterSalesSnList": parent_after_sales_sn_list,
            "pageNo": page_no,
            "pageSize": page_size,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.aftersales.parentaftersales.detail.get")
    def parent_aftersales_detail(
        self,
        parent_order_sn: str,
        parent_after_sales_sn: str,
        **kwargs
    ) -> ApiResponse:
        """
        查询父售后单详情（temu.aftersales.parentaftersales.detail.get）。
        :param parent_order_sn: 父订单号，必填
        :param parent_after_sales_sn: 父售后单号，必填
        其余参数通过 kwargs 传递。
        This interface provides detailed information on after-sales orders in real time.
        """
        data = {
            "parentOrderSn": parent_order_sn,
            "parentAfterSalesSn": parent_after_sales_sn,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.aftersales.refund.issue")
    def refund_issue(
        self,
        parent_after_sales_sn: str,
        parent_order_sn: str,
        open_api_refund_type: int,
        **kwargs
    ) -> ApiResponse:
        """
        售后退款处理（temu.aftersales.refund.issue）。
        :param parent_after_sales_sn: 售后父单号，必填
        :param parent_order_sn: 订单号，必填
        :param open_api_refund_type: 退款类型，必填（1-全额退款）
        其余参数通过 kwargs 传递。
        This interface enables merchants to efficiently process refund requests.
        """
        data = {
            "parentAfterSalesSn": parent_after_sales_sn,
            "parentOrderSn": parent_order_sn,
            "openApiRefundType": open_api_refund_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.aftersales.parentreturnorder.get")
    def parent_return_order(
        self,
        parent_after_sales_sn: str,
        after_sales_sn: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询父售后单退货物流信息（bg.aftersales.parentreturnorder.get）。
        :param parent_after_sales_sn: 售后父单号，必填
        :param after_sales_sn: 售后单号，选填
        其余参数通过 kwargs 传递。
        This interface provides detailed return logistics information for a set of after-sales service requests.
        """
        data = {
            "parentAfterSalesSn": parent_after_sales_sn,
            "afterSalesSn": after_sales_sn,
        }
        return self._request(data={**data, **kwargs})