from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Fulfillment(BaseAPI):
    @action("bg.order.fulfillment.info.sync")
    def fulfillment_info_sync(
        self,
        fulfillment_type: int,
        order_sn: str = None,
        warehouse_operation_status: int = None,
        operation_time: int = None,
        tracking_number: str = None,
        warehouse_brand_name: str = None,
        warehouse_name: str = None,
        warehouse_region1: str = None,
        warehouse_region2: str = None,
        warehouse_region3: str = None,
        warehouse_region4: str = None,
        warehouse_address_line1: str = None,
        warehouse_address_line2: str = None,
        warehouse_post_code: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        同步订单履约信息（bg.order.fulfillment.info.sync）。
        :param fulfillment_type: 履约类型，必填（0-FBA订单，1-非FBA订单）
        :param order_sn: 订单号（子订单号），选填
        :param warehouse_operation_status: 仓库操作状态，选填（0-已发货，1-已妥投）
        :param operation_time: 仓库操作时间，选填
        :param tracking_number: 物流单号，选填
        :param warehouse_brand_name: 仓库品牌名，选填
        :param warehouse_name: 仓库名称，选填
        :param warehouse_region1/2/3/4: 仓库区域，选填
        :param warehouse_address_line1/2: 仓库地址，选填
        :param warehouse_post_code: 仓库邮编，选填
        其余参数通过 kwargs 传递。
        You can call this interface to synchronize order fulfillment information.
        """
        data = {
            "fulfillmentType": fulfillment_type,
            "orderSn": order_sn,
            "warehouseOperationStatus": warehouse_operation_status,
            "operationTime": operation_time,
            "trackingNumber": tracking_number,
            "warehouseBrandName": warehouse_brand_name,
            "warehouseName": warehouse_name,
            "warehouseRegion1": warehouse_region1,
            "warehouseRegion2": warehouse_region2,
            "warehouseRegion3": warehouse_region3,
            "warehouseRegion4": warehouse_region4,
            "warehouseAddressLine1": warehouse_address_line1,
            "warehouseAddressLine2": warehouse_address_line2,
            "warehousePostCode": warehouse_post_code,
        }
        return self._request(data={**data, **kwargs})

    
    @action("bg.logistics.shipment.v2.confirm")
    def shipment_v2_confirm(
        self,
        send_type: int,
        send_request_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        订单发货确认（bg.logistics.shipment.v2.confirm）。
        :param send_type: 发货类型，必填（0-整单一包裹，1-部分多包裹，2-多单一包裹）
        :param send_request_list: 发货包裹详情列表，必填
        其余参数通过 kwargs 传递。
        The bg.logistic.shipment.v2.confirm interface is designed to synchronize and return order fulfillment information.
        """
        data = {
            "sendType": send_type,
            "sendRequestList": send_request_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.sub.confirm")
    def shipment_sub_confirm(
        self,
        main_package_sn: str,
        send_sub_request_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        子包裹发货确认（bg.logistics.shipment.sub.confirm）。
        :param main_package_sn: 已发货主包裹号，必填
        :param send_sub_request_list: 子包裹信息列表，选填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.sub.confirm interface should only be used in scenarios where the smallest sku needs to be shipped as split packages.
        """
        data = {
            "mainPackageSn": main_package_sn,
            "sendSubRequestList": send_sub_request_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.shippingtype.update")
    def shipment_shippingtype_update(
        self,
        edit_package_request_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        更新物流包裹的物流公司及运单号（bg.logistics.shipment.shippingtype.update）。
        :param edit_package_request_list: 包裹更新请求列表，选填，每项需包含 packageSn、trackingNumber、shipCompanyId
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.shippingtype.update interface is used by sellers to update logistics tracking numbers.
        """
        data = {
            "editPackageRequestList": edit_package_request_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.create")
    def shipment_create(
        self,
        send_type: int,
        send_request_list: list = None,
        ship_later: bool = None,
        ship_later_limit_time: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        在线下单获取包裹号（bg.logistics.shipment.create）。
        :param send_type: 发货类型，必填（0-整单一包裹，1-部分多包裹，2-多单一包裹）
        :param send_request_list: 包裹信息列表，选填
        :param ship_later: 是否稍后发货，选填
        :param ship_later_limit_time: 稍后发货截止时间（24/48/72/96/120小时），选填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.create interface is for sellers to place online logistics orders and receive package numbers.
        """
        data = {
            "sendType": send_type,
            "sendRequestList": send_request_list,
            "shipLater": ship_later,
            "shipLaterLimitTime": ship_later_limit_time,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.result.get")
    def shipment_result_get(
        self,
        package_sn_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询物流下单结果（bg.logistics.shipment.result.get）。
        :param package_sn_list: 包裹号列表，选填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.result.get interface is for sellers to query the result of placing online logistics orders.
        """
        data = {
            "packageSnList": package_sn_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.update")
    def shipment_update(
        self,
        retry_send_package_request_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        重新下单/补单接口（bg.logistics.shipment.update）。
        :param retry_send_package_request_list: 需重试的包裹信息列表，选填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.update interface is for sellers to create shipment logistics orders later, and to re-order online if the order fails.
        """
        data = {
            "retrySendPackageRequestList": retry_send_package_request_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.document.get")
    def shipment_document_get(
        self,
        document_type: str = None,
        package_sn_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        获取快递面单（bg.logistics.shipment.document.get）。
        :param document_type: 面单类型，选填（如 SHIPPING_LABEL_PDF）
        :param package_sn_list: 需要获取面单的包裹号列表，选填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.document.get interface is for sellers to obtain the express delivery waybill.
        """
        data = {
            "documentType": document_type,
            "packageSnList": package_sn_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipment.v2.get")
    def shipment_v2_get(
        self,
        parent_order_sn: str,
        order_sn: str,
        **kwargs
    ) -> ApiResponse:
        """
        查询自发货订单发货信息（bg.logistics.shipment.v2.get）。
        :param parent_order_sn: 父订单号，必填
        :param order_sn: 子订单号，必填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipment.v2.get interface is for sellers to verify shipped info after self-fulfillment.
        """
        data = {
            "parentOrderSn": parent_order_sn,
            "orderSn": order_sn,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.order.unshipped.package.get")
    def unshipped_package_get(
        self,
        page_number: int,
        page_size: int,
        parent_order_sn_list: list = None,
        order_sn_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询已履约未发货包裹信息（bg.order.unshipped.package.get）。
        :param page_number: 页码，必填
        :param page_size: 每页数量，必填
        :param parent_order_sn_list: 父订单号列表，选填
        :param order_sn_list: 子订单号列表，选填
        其余参数通过 kwargs 传递。
        The bg.order.unshipped.package.get interface is for sellers to query information about packages that have been fulfilled successfully by Temu-integrated channel.
        """
        data = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "parentOrderSnList": parent_order_sn_list,
            "orderSnList": order_sn_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shipped.package.confirm")
    def shipped_package_confirm(
        self,
        package_send_info_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        批量确认已履约未发货包裹为已发货（bg.logistics.shipped.package.confirm）。
        :param package_send_info_list: 需确认发货的包裹信息列表，必填
        其余参数通过 kwargs 传递。
        The bg.logistics.shipped.package.confirm interface is for sellers to support batch conversion of packages to shipped status.
        """
        data = {
            "packageSendInfoList": package_send_info_list,
        }
        return self._request(data={**data, **kwargs})