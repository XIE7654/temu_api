from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Price(BaseAPI):
    @action("temu.local.goods.recommendedprice.query")
    def recommended_price_query(
        self,
        recommended_price_type: int,
        goods_id_list: list,
        language: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询商品推荐供货价（temu.local.goods.recommendedprice.query）。
        :param recommended_price_type: 推荐价类型，必填（10-低流量，20-限流）
        :param goods_id_list: 商品ID列表，必填，1-100个
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Support merchants in querying the recommended supply prices.
        """
        data = {
            "recommendedPriceType": recommended_price_type,
            "goodsIdList": goods_id_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.appealorder.record.query")
    def appealorder_record_query(
        self,
        sku_id: int,
        page_no: int = None,
        page_size: int = None,
        language: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询商品申诉单记录（temu.local.goods.appealorder.record.query）。
        :param sku_id: SKU ID，必填
        :param page_no: 页码，选填
        :param page_size: 每页数量，选填（小于100）
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Support merchants in querying appeal order records.
        """
        data = {
            "skuId": sku_id,
            "pageNo": page_no,
            "pageSize": page_size,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.appealorder.create")
    def appealorder_create(
        self,
        goods_id: int,
        merchant_appeal_reason_code_list: list,
        sku_info_list: list,
        language: str = None,
        external_link_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        创建商品申诉单（temu.local.goods.appealorder.create）。
        :param goods_id: 商品ID，必填
        :param merchant_appeal_reason_code_list: 申诉原因编码列表，必填
        :param sku_info_list: SKU信息列表，必填
        :param language: 语言，选填
        :param external_link_list: 外部链接列表，选填
        其余参数通过 kwargs 传递。
        Support merchants in appealing against the recommended supply prices of low traffic goods.
        """
        data = {
            "goodsId": goods_id,
            "merchantAppealReasonCodeList": merchant_appeal_reason_code_list,
            "skuInfoList": sku_info_list,
            "language": language,
            "externalLinkList": external_link_list,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.appealorder.query")
    def appealorder_query(
        self,
        tab_code: int,
        page_no: int = None,
        page_size: int = None,
        language: str = None,
        goods_id_list: list = None,
        sku_id_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询商品申诉单（temu.local.goods.appealorder.query）。
        :param tab_code: 申诉单tab编码，必填（0-全部，10-进行中，20-已接受，30-需处理，40-已终止）
        :param page_no: 页码，选填
        :param page_size: 每页数量，选填（小于100）
        :param language: 语言，选填
        :param goods_id_list: 商品ID列表，选填
        :param sku_id_list: SKU ID列表，选填
        其余参数通过 kwargs 传递。
        Support merchants in querying appeal orders.
        """
        data = {
            "tabCode": tab_code,
            "pageNo": page_no,
            "pageSize": page_size,
            "language": language,
            "goodsIdList": goods_id_list,
            "skuIdList": sku_id_list,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.priceorder.reject")
    def priceorder_reject(
        self,
        price_order_base_list: list,
        language: str = None,
        reject_delist: bool = None,
        **kwargs
    ) -> ApiResponse:
        """
        拒绝商品定价单（temu.local.goods.priceorder.reject）。
        :param price_order_base_list: 定价单列表，必填
        :param language: 语言，选填
        :param reject_delist: 是否拒绝并下架sku，选填
        其余参数通过 kwargs 传递。
        Support merchants in rejecting price orders.
        """
        data = {
            "priceOrderBaseList": price_order_base_list,
            "language": language,
            "rejectDelist": reject_delist,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.sku.list.price.query")
    def sku_list_price_query(
        self,
        query_supplier_price_base_list: list,
        language: str = None,
        **kwargs
    ) -> ApiResponse:
        """
        批量查询本地商品SKU最新供货价（bg.local.goods.sku.list.price.query）。
        :param query_supplier_price_base_list: 查询供货价基础信息列表，必填
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        This is an API for batch querying the latest supply prices of SKUs for local-to-local goods.
        """
        data = {
            "querySupplierPriceBaseList": query_supplier_price_base_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.priceorder.change.sku.price")
    def change_sku_price(
        self,
        goods_id: int,
        change_sku_price_dto_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        批量修改SKU底价（bg.local.goods.priceorder.change.sku.price）。
        :param goods_id: 商品ID，必填
        :param change_sku_price_dto_list: SKU调价信息及原因列表，必填
        其余参数通过 kwargs 传递。
        Support merchants within the white list to modify sku base prices in batches.
        """
        data = {
            "goodsId": goods_id,
            "changeSkuPriceDTOList": change_sku_price_dto_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.priceorder.query")
    def priceorder_query(
        self,
        page: int = None,
        size: int = None,
        price_order_type: int = None,
        price_order_sub_type: int = None,
        goods_name: str = None,
        goods_id: str = None,
        price_order_sn_list: list = None,
        order_by: str = None,
        order_by_type: int = None,
        goods_create_time_from: int = None,
        goods_create_time_to: int = None,
        price_order_create_time_from: int = None,
        price_order_create_time_to: int = None,
        goods_id_list: list = None,
        status: int = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询定价单列表（bg.local.goods.priceorder.query）。
        :param page: 页码，选填
        :param size: 每页数量，选填（小于100）
        :param price_order_type: 定价类型，选填
        :param price_order_sub_type: 定价子类型，选填
        :param goods_name: 商品名称，选填
        :param goods_id: 商品ID，选填
        :param price_order_sn_list: 定价单号列表，选填
        :param order_by: 排序字段，选填
        :param order_by_type: 排序类型，选填
        :param goods_create_time_from: 商品创建起始时间，选填
        :param goods_create_time_to: 商品创建结束时间，选填
        :param price_order_create_time_from: 定价单创建起始时间，选填
        :param price_order_create_time_to: 定价单创建结束时间，选填
        :param goods_id_list: 商品ID列表，选填
        :param status: 定价单状态，选填
        其余参数通过 kwargs 传递。
        Support merchants within the white list to query the price offer list.
        """
        data = {
            "page": page,
            "size": size,
            "priceOrderType": price_order_type,
            "priceOrderSubType": price_order_sub_type,
            "goodsName": goods_name,
            "goodsId": goods_id,
            "priceOrderSnList": price_order_sn_list,
            "orderBy": order_by,
            "orderByType": order_by_type,
            "goodsCreateTimeFrom": goods_create_time_from,
            "goodsCreateTimeTo": goods_create_time_to,
            "priceOrderCreateTimeFrom": price_order_create_time_from,
            "priceOrderCreateTimeTo": price_order_create_time_to,
            "goodsIdList": goods_id_list,
            "status": status,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.priceorder.accept")
    def priceorder_accept(
        self,
        price_order_info_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        接受定价单（bg.local.goods.priceorder.accept）。
        :param price_order_info_list: 定价单信息列表，必填
        其余参数通过 kwargs 传递。
        Support merchants within the white list to accept the price offer through the interface.
        """
        data = {
            "priceOrderInfoList": price_order_info_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.priceorder.negotiate")
    def priceorder_negotiate(
        self,
        price_order_id: int,
        negotiated_price_sku_list: list,
        goods_id: int,
        price_commit_version: int,
        price_commit_id: int,
        external_link_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        议价定价单（bg.local.goods.priceorder.negotiate）。
        支持白名单内商家通过接口进行议价。
        :param price_order_id: 定价单ID，必填
        :param negotiated_price_sku_list: SKU议价信息列表，必填
        :param goods_id: 商品ID，必填
        :param price_commit_version: 价格提交版本，必填
        :param price_commit_id: 价格提交ID，必填
        :param external_link_list: 外部链接列表，选填
        其余参数通过 kwargs 传递。
        Negotiate price order (bg.local.goods.priceorder.negotiate).
        Support merchants within the whitelist to negotiate price through interfaces.
        """
        data = {
            "priceOrderId": price_order_id,
            "negotiatedPriceSkuList": negotiated_price_sku_list,
            "goodsId": goods_id,
            "priceCommitVersion": price_commit_version,
            "priceCommitId": price_commit_id,
            "externalLinkList": external_link_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.order.amount.query")
    def amount_query(
        self,
        parent_order_sn: str,
        **kwargs
    ) -> ApiResponse:
        """
        查询订单供货价信息（bg.order.amount.query）。
        为自研ERP提供订单对应的供货价信息。
        :param parent_order_sn: 父订单号，必填
        其余参数通过 kwargs 传递。
        Query order supply price info (bg.order.amount.query).
        Provide the supply price information corresponding to the orders for the self-developed ERP.
        """
        data = {
            "parentOrderSn": parent_order_sn,
        }
        return self._request(data={**data, **kwargs})
