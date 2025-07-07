from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Order(BaseAPI):

    @action("bg.order.list.v2.get")
    def list_orders_v2(
        self,
        page_number: int = 1,
        page_size: int = 10,
        parent_order_status: int = None,
        parent_order_sn_list: list = None,
        create_after: int = None,
        create_before: int = None,
        expect_ship_latest_time_start: int = None,
        expect_ship_latest_time_end: int = None,
        update_at_start: int = None,
        update_at_end: int = None,
        region_id: int = None,
        fulfillment_type_list: list = None,
        parent_order_label: list = None,
        sortby: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        The bg.order.list.v2.get interface is designed to support batch return of corresponding order lists based on filtering criteria.
        参数说明：
            page_number: 分页页码，默认1
            page_size: 分页大小，默认10，最大100
            parent_order_status: 父订单状态，默认全部
            parent_order_sn_list: 父订单号列表，最多20个
            create_after: 父订单创建起始时间（秒）
            create_before: 父订单创建结束时间（秒）
            expect_ship_latest_time_start: 期望最晚发货起始时间（秒）
            expect_ship_latest_time_end: 期望最晚发货结束时间（秒）
            update_at_start: 订单更新时间起始（秒）
            update_at_end: 订单更新时间结束（秒）
            region_id: 区域ID
            fulfillment_type_list: 履约类型列表
            parent_order_label: 父订单标签
            sortby: 排序字段
        其余参数通过 kwargs 传递。
        """
        data = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "parentOrderStatus": parent_order_status,
            "parentOrderSnList": parent_order_sn_list,
            "createAfter": create_after,
            "createBefore": create_before,
            "expectShipLatestTimeStart": expect_ship_latest_time_start,
            "expectShipLatestTimeEnd": expect_ship_latest_time_end,
            "updateAtStart": update_at_start,
            "updateAtEnd": update_at_end,
            "regionId": region_id,
            "fulfillmentTypeList": fulfillment_type_list,
            "parentOrderLabel": parent_order_label,
            "sortby": sortby,
        }
        # 移除值为 None 的参数
        return self._request(data={**data, **kwargs})

    @action("bg.order.detail.v2.get")
    def detail_order_v2(
        self,
        parent_order_sn: str,
        fulfillment_type_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        获取指定父订单的详细信息（bg.order.detail.v2.get）。
        :param parent_order_sn: 父订单号，必填
        :param fulfillment_type_list: 履约类型列表，选填
        其余参数通过 kwargs 传递。
        This interface allows merchants to retrieve detailed information about a specific order.
        """
        data = {
            "parentOrderSn": parent_order_sn,
            "fulfillmentTypeList": fulfillment_type_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.order.shippinginfo.v2.get")
    def shippinginfo_order_v2(
        self,
        parent_order_sn: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        获取指定父订单的收货地址信息（bg.order.shippinginfo.v2.get）。
        :param parent_order_sn: 父订单号，必填
        其余参数通过 kwargs 传递。
        This interface retrieves shipping address information for a specific order.
        """
        data = {
            "parentOrderSn": parent_order_sn,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.order.combinedshipment.list.get")
    def combinedshipment_list_order(
        self,
        **kwargs
    ) -> ApiResponse:
        """
        获取可合并发货的父订单分组（bg.order.combinedshipment.list.get）。
        其余参数通过 kwargs 传递。
        This interface retrieves combined shipping groups including lists of parent orders that can be combined for shipping.
        """
        data = {}
        return self._request(data={**data, **kwargs})

    @action("bg.order.customization.get")
    def customization_order(
        self,
        order_sn_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        批量获取订单定制商品内容信息（bg.order.customization.get）。
        :param order_sn_list: 订单号列表，最多10个，选填
        其余参数通过 kwargs 传递。
        Self developed sellers and third-party ISVs obtain customized product content information in bulk through Open API.
        """
        data = {
            "orderSnList": order_sn_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.order.decryptshippinginfo.get")
    def decryptshippinginfo_order(
        self,
        parent_order_sn: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        获取指定父订单的敏感收货地址信息（bg.order.decryptshippinginfo.get）。
        :param parent_order_sn: 父订单号，选填
        其余参数通过 kwargs 传递。
        This interface retrieves sensitive shipping address information for a specific order.
        """
        data = {
            "parentOrderSn": parent_order_sn,
        }
        return self._request(data={**data, **kwargs})

