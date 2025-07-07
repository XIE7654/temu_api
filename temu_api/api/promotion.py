from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action


class Promotion(BaseAPI):
    @action("bg.promotion.activity.query")
    def activity_query(
        self,
        page_number: int = 1,
        page_size: int = 10,
        activity_type: int = None,
        activity_end_time: int = None,
        activity_id_list: list = None,
        activity_status: int = None,
        activity_start_time: int = None,
        only_query_joined_activity: bool = None,
        **kwargs
    ) -> ApiResponse:
        """
        查询本地活动列表（bg.promotion.activity.query）。
        :param page_number: 分页页码，必填，默认1
        :param page_size: 分页大小，必填，默认10，最大100
        :param activity_type: 活动类型，必填
        :param activity_end_time: 活动结束时间，选填
        :param activity_id_list: 活动ID列表，选填
        :param activity_status: 活动状态，选填
        :param activity_start_time: 活动开始时间，选填
        :param only_query_joined_activity: 是否只查已参与活动，选填
        其余参数通过 kwargs 传递。
        query the local to local activity
        """
        data = {
            "pageNumber": page_number,
            "pageSize": page_size,
            "activityType": activity_type,
            "activityEndTime": activity_end_time,
            "activityIdList": activity_id_list,
            "activityStatus": activity_status,
            "activityStartTime": activity_start_time,
            "onlyQueryJoinedActivity": only_query_joined_activity,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.promotion.activity.candidate.goods.query")
    def activity_candidate_goods_query(
        self,
        activity_id: int,
        page_number: int = 1,
        page_size: int = 10,
        **kwargs
    ) -> ApiResponse:
        """
        查询本地活动候选商品列表（bg.promotion.activity.candidate.goods.query）。
        :param activity_id: 活动ID，必填
        :param page_number: 分页页码，必填，默认1
        :param page_size: 分页大小，必填，默认10，最大100
        其余参数通过 kwargs 传递。
        the local to local activity candidate goods
        """
        data = {
            "activityId": activity_id,
            "pageNumber": page_number,
            "pageSize": page_size,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.promotion.activity.goods.query")
    def activity_goods_query(
        self,
        activity_id: int,
        page_number: int = 1,
        page_size: int = 10,
        **kwargs
    ) -> ApiResponse:
        """
        查询本地活动商品列表（bg.promotion.activity.goods.query）。
        :param activity_id: 活动ID，必填
        :param page_number: 分页页码，必填，默认1
        :param page_size: 分页大小，必填，默认10，最大100
        其余参数通过 kwargs 传递。
        query the local to local activity goods
        """
        data = {
            "activityId": activity_id,
            "pageNumber": page_number,
            "pageSize": page_size,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.promotion.activity.goods.enroll")
    def activity_goods_enroll(
        self,
        activity_id: int,
        enroll_goods: dict,
        **kwargs
    ) -> ApiResponse:
        """
        报名本地活动商品（bg.promotion.activity.goods.enroll）。
        :param activity_id: 活动ID，必填
        :param enroll_goods: 报名商品信息，必填，dict类型
        其余参数通过 kwargs 传递。
        enroll products in the local to local activity
        """
        data = {
            "activityId": activity_id,
            "enrollGoods": enroll_goods,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.promotion.activity.goods.operation.query")
    def activity_goods_operation_query(
        self,
        draft_id_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        查询本地活动商品操作结果（bg.promotion.activity.goods.operation.query）。
        :param draft_id_list: 商品报名草稿ID列表，必填
        其余参数通过 kwargs 传递。
        query the result of operation in the local to local activity
        """
        data = {
            "draftIdList": draft_id_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.promotion.activity.goods.update")
    def activity_goods_update(
        self,
        activity_id: int,
        goods_id: int,
        operate_type: int,
        trace_code: str = None,
        activity_quantity: int = None,
        update_sku_list: list = None,
        add_sku_list: list = None,
        **kwargs
    ) -> ApiResponse:
        """
        更新本地活动商品信息（bg.promotion.activity.goods.update）。
        :param activity_id: 活动ID，必填
        :param goods_id: 商品ID，必填
        :param operate_type: 操作类型，必填（10-更新价格，20-更新数量，30-下架，40-新增SKU）
        :param trace_code: 幂等键，选填
        :param activity_quantity: 活动数量，operate_type=20时必填
        :param update_sku_list: 更新SKU信息，operate_type=10/40时选填
        :param add_sku_list: 新增SKU信息，operate_type=40时选填
        其余参数通过 kwargs 传递。
        update activity goods information in the local to local activity
        """
        data = {
            "activityId": activity_id,
            "goodsId": goods_id,
            "operateType": operate_type,
            "traceCode": trace_code,
            "activityQuantity": activity_quantity,
            "updateSkuList": update_sku_list,
            "addSkuList": add_sku_list,
        }
        return self._request(data={**data, **kwargs})