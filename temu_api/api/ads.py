from temu_api.api.base import BaseAPI
from temu_api.utils.api_response import ApiResponse
from temu_api.utils.helpers import action

class Ads(BaseAPI):

    @action("temu.searchrec.ad.roas.pred")
    def roas_pred(
        self,
        goods_info_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        广告ROAS预测（temu.searchrec.ad.roas.pred）。
        :param goods_info_list: 商品信息列表，必填，每项需包含 goodsId
        其余参数通过 kwargs 传递。
        Advertising roas prediction
        """
        data = {
            "goodsInfoList": goods_info_list,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.reports.mall.query")
    def reports_mall_query(
        self,
        start_ts: int,
        end_ts: int,
        **kwargs
    ) -> ApiResponse:
        """
        广告整体数据报表（商场维度）（temu.searchrec.ad.reports.mall.query）。
        :param start_ts: 查询起始时间，毫秒级时间戳，必填
        :param end_ts: 查询结束时间，毫秒级时间戳，必填
        其余参数通过 kwargs 传递。
        Advertisement overall data report (mall dimension)
        """
        data = {
            "startTs": start_ts,
            "endTs": end_ts,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.reports.goods.query")
    def reports_goods_query(
        self,
        start_ts: int,
        end_ts: int,
        goods_id: int,
        **kwargs
    ) -> ApiResponse:
        """
        广告商品数据报表（商品维度）（temu.searchrec.ad.reports.goods.query）。
        :param start_ts: 查询起始时间，毫秒级时间戳，必填
        :param end_ts: 查询结束时间，毫秒级时间戳，必填
        :param goods_id: 商品ID，必填
        其余参数通过 kwargs 传递。
        Advertisement goods data report (goods dimension)
        """
        data = {
            "startTs": start_ts,
            "endTs": end_ts,
            "goodsId": goods_id,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.create")
    def ad_create(
        self,
        create_ad_reqs: list,
        **kwargs
    ) -> ApiResponse:
        """
        创建广告（temu.searchrec.ad.create）。
        :param create_ad_reqs: 广告创建参数列表，必填，每项需包含 roas、goodsId、budget
        其余参数通过 kwargs 传递。
        Advertisement creation
        """
        data = {
            "createAdReqs": create_ad_reqs,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.detail.query")
    def ad_detail_query(
        self,
        goods_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        广告活动详情查询（temu.searchrec.ad.detail.query）。
        :param goods_list: 商品ID列表，必填
        其余参数通过 kwargs 传递。
        Advertising campaign details query
        """
        data = {
            "goodsList": goods_list,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.log.query")
    def ad_log_query(
        self,
        goods_id: int,
        start_time: int,
        end_time: int,
        **kwargs
    ) -> ApiResponse:
        """
        广告日志查询（temu.searchrec.ad.log.query）。
        :param goods_id: 商品ID，必填
        :param start_time: 查询起始时间，毫秒级时间戳，必填
        :param end_time: 查询结束时间，毫秒级时间戳，必填
        其余参数通过 kwargs 传递。
        Advertisement log query
        """
        data = {
            "goodsId": goods_id,
            "startTime": start_time,
            "endTime": end_time,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.goods.create.query")
    def ad_goods_create_query(
        self,
        goods_id_list: list,
        **kwargs
    ) -> ApiResponse:
        """
        广告商品可创建查询（temu.searchrec.ad.goods.create.query）。
        :param goods_id_list: 商品ID列表，必填
        其余参数通过 kwargs 传递。
        Advertising goods can create query
        """
        data = {
            "goodsIdList": goods_id_list,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.searchrec.ad.modify")
    def ad_modify(
        self,
        modify_ad_dto: dict,
        status: int,
        **kwargs
    ) -> ApiResponse:
        """
        广告修改（temu.searchrec.ad.modify）。
        :param modify_ad_dto: 修改广告参数，必填，dict类型，需包含 goodsId、status（1:删除, 2:暂停, 3:开启, 4:改预算, 5:改roas），选填 roas、budget
        :param status: 操作类型，必填，1-删除，2-暂停，3-开启，4-修改预算，5-修改roas
        其余参数通过 kwargs 传递。
        Advertisement modify
        """
        data = {
            "modifyAdDTO": modify_ad_dto,
            "status": status,
        }
        return self._request(data={**data, **kwargs})
