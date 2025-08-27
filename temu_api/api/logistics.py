from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Logistics(BaseAPI):

    @action("bg.logistics.warehouse.list.get")
    def warehouse_list(self, **kwargs) -> ApiResponse:
        """
        获取店铺仓库信息（bg.logistics.warehouse.list.get）。
        Sellers can use this API to obtain the shop's warehouse information.
        其余参数通过 kwargs 传递。
        """
        data = {}
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.companies.get")
    def companies(self, region_id: int, **kwargs) -> ApiResponse:
        """
        获取指定区域支持发货的全部物流公司（bg.logistics.companies.get）。
        :param region_id: 区域ID，必填
        Obtain full logistics providers that support shipping at the corresponding region.
        其余参数通过 kwargs 传递。
        """
        data = {
            "regionId": region_id,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.logistics.shippingservices.get")
    def shipping_services(
        self,
        warehouse_id: str,
        order_sn_list: list,
        weight: str,
        weight_unit: str,
        length: str,
        width: str,
        height: str,
        dimension_unit: str,
        extend_weight: str = None,
        extend_weight_unit: str = None,
        signature_on_delivery: bool = None,
        invoice_access_key: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询包裹支持的物流服务商（bg.logistics.shippingservices.get）。
        :param warehouse_id: 仓库ID，必填
        :param order_sn_list: 包裹内订单号列表，必填
        :param weight: 包裹重量，必填
        :param weight_unit: 重量单位，必填（美国为lb，其他国家为kg）
        :param length: 包裹长度，两位小数，必填
        :param width: 包裹宽度，两位小数，必填
        :param height: 包裹高度，两位小数，必填
        :param dimension_unit: 尺寸单位，必填（美国为in，其他国家为cm）
        :param extend_weight: 扩展重量（美国本地订单小数部分），选填
        :param extend_weight_unit: 扩展重量单位（美国本地为oz），选填
        :param signature_on_delivery: 是否需要签收，选填
        :param invoice_access_key: 巴西订单发票编号，选填（仅巴西订单必填）
        其余参数通过 kwargs 传递。
        The bg.logistics.shippingservices.get interface is for sellers to retrieve supported shipping carriers based on package dimensions and weight.
        """
        data = {
            "warehouseId": warehouse_id,
            "orderSnList": order_sn_list,
            "weight": weight,
            "weightUnit": weight_unit,
            "length": length,
            "width": width,
            "height": height,
            "dimensionUnit": dimension_unit,
            "extendWeight": extend_weight,
            "extendWeightUnit": extend_weight_unit,
            "signatureOnDelivery": signature_on_delivery,
            "invoiceAccessKey": invoice_access_key,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.logistics.shiplogisticstype.get")
    def ship_logistics_type(self, region_id: int, **kwargs) -> ApiResponse:
        """
        获取所有在线发货物流类型信息（temu.logistics.shiplogisticstype.get）。
        :param region_id: 区域ID，必填
        You can get all online ship logistics type information from this api.
        其余参数通过 kwargs 传递。
        """
        data = {
            "regionId": region_id,
        }
        return self._request(data={**data, **kwargs})