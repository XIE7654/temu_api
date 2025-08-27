from temu_api.api.base import BaseAPI
from temu_api.utils.helpers import action


class Product(BaseAPI):
    @action("temu.local.goods.illegal.vocabulary.check")
    def illegal_vocabulary_check(
        self,
        goods_name: str = None,
        goods_desc: str = None,
        bullet_points: list = None,
        **kwargs
    ):
        """
        违规词预检查（temu.local.goods.illegal.vocabulary.check）。
        :param goods_name: 商品名称内容，选填
        :param goods_desc: 商品描述内容，选填
        :param bullet_points: 卖点内容列表，选填
        其余参数通过 kwargs 传递。
        Check illegal vocabulary (temu.local.goods.illegal.vocabulary.check).
        """
        data = {
            "goodsName": goods_name,
            "goodsDesc": goods_desc,
            "bulletPoints": bullet_points,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.sku.net.content.unit.query")
    def sku_net_content_unit_query(
        self,
        language: str = None,
        **kwargs
    ):
        """
        查询 SKU 转换类型的净含量单位多语言信息（temu.local.goods.sku.net.content.unit.query）。
        This API allows sellers to get multi-language information of SKU transfer type net content unit.

        :param language: 语言，可选。例如 "en"、"zh" 等
        :param kwargs: 额外可选参数
        """
        data = {}
        if language:
            data["language"] = language
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.delete")
    def delete_goods(
        self,
        goods_id: int,
        **kwargs
    ):
        """
        删除商品（temu.local.goods.delete）。
        :param goods_id: 商品ID，必填
        其余参数通过 kwargs 传递。
        Product deletion (temu.local.goods.delete).
        """
        data = {
            "goodsId": goods_id,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.sku.list.retrieve")
    def sku_list_retrieve(
        self,
        sku_search_type: str,
        page_size: int = None,
        page_token: str = None,
        order_field: str = None,
        order_type: int = None,
        goods_id_list: list = None,
        out_goods_sn_list: list = None,
        sku_id_list: list = None,
        out_sku_sn_list: list = None,
        cat_id_list: list = None,
        goods_name: str = None,
        goods_create_time_from: int = None,
        goods_create_time_to: int = None,
        sku_status_change_time_from: int = None,
        sku_status_change_time_to: int = None,
        goods_search_tags: list = None,
        **kwargs
    ):
        """
        本地SKU列表检索（temu.local.sku.list.retrieve）。
        :param sku_search_type: SKU状态筛选，必填（ACTIVE, INACTIVE, INCOMPLETE, DRAFT, DELETED）
        :param page_size: 每页数量，选填，最大100，默认25
        :param page_token: 分页token，选填
        :param order_field: 排序字段，选填（如 create_time）
        :param order_type: 排序类型，选填（0-降序，1-升序，默认0）
        :param goods_id_list: 商品ID列表，选填，最多100
        :param out_goods_sn_list: 外部商品编码列表，选填，最多100
        :param sku_id_list: SKU ID列表，选填，最多200
        :param out_sku_sn_list: 外部SKU编码列表，选填，最多200
        :param cat_id_list: 类目ID列表，选填，最多100
        :param goods_name: 商品名称，选填
        :param goods_create_time_from: 商品创建起始时间（毫秒），选填
        :param goods_create_time_to: 商品创建结束时间（毫秒），选填
        :param sku_status_change_time_from: SKU状态变更起始时间（毫秒），选填
        :param sku_status_change_time_to: SKU状态变更结束时间（毫秒），选填
        :param goods_search_tags: 商品搜索标签，选填（如1-低流量, 4-限流）
        其余参数通过 kwargs 传递。
        Local SKU list search (temu.local.sku.list.retrieve).
        """
        data = {
            "skuSearchType": sku_search_type,
            "pageSize": page_size,
            "pageToken": page_token,
            "orderField": order_field,
            "orderType": order_type,
            "goodsIdList": goods_id_list,
            "outGoodsSnList": out_goods_sn_list,
            "skuIdList": sku_id_list,
            "outSkuSnList": out_sku_sn_list,
            "catIdList": cat_id_list,
            "goodsName": goods_name,
            "goodsCreateTimeFrom": goods_create_time_from,
            "goodsCreateTimeTo": goods_create_time_to,
            "skuStatusChangeTimeFrom": sku_status_change_time_from,
            "skuStatusChangeTimeTo": sku_status_change_time_to,
            "goodsSearchTags": goods_search_tags,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.list.retrieve")
    def goods_list_retrieve(
        self,
        goods_search_type: str,
        page_size: int = None,
        page_token: str = None,
        order_field: str = None,
        order_type: int = None,
        goods_id_list: list = None,
        out_goods_sn_list: list = None,
        sku_id_list: list = None,
        out_sku_sn_list: list = None,
        cat_id_list: list = None,
        goods_name: str = None,
        goods_create_time_from: int = None,
        goods_create_time_to: int = None,
        goods_status_change_time_from: int = None,
        goods_status_change_time_to: int = None,
        goods_search_tags: list = None,
        **kwargs
    ):
        """
        本地商品列表检索（temu.local.goods.list.retrieve）。
        :param goods_search_type: 商品状态筛选，必填（ALL, ACTIVE, INACTIVE, INCOMPLETE, DRAFT, DELETED）
        :param page_size: 每页数量，选填，最大100，默认25
        :param page_token: 分页token，选填
        :param order_field: 排序字段，选填（如 create_time）
        :param order_type: 排序类型，选填（0-降序，1-升序，默认0）
        :param goods_id_list: 商品ID列表，选填，最多100
        :param out_goods_sn_list: 外部商品编码列表，选填，最多100
        :param sku_id_list: SKU ID列表，选填，最多200
        :param out_sku_sn_list: 外部SKU编码列表，选填，最多200
        :param cat_id_list: 类目ID列表，选填，最多100
        :param goods_name: 商品名称，选填
        :param goods_create_time_from: 商品创建起始时间（毫秒），选填
        :param goods_create_time_to: 商品创建结束时间（毫秒），选填
        :param goods_status_change_time_from: 商品状态变更起始时间（毫秒），选填
        :param goods_status_change_time_to: 商品状态变更结束时间（毫秒），选填
        :param goods_search_tags: 商品搜索标签，选填（如1-低流量, 4-限流）
        其余参数通过 kwargs 传递。
        Local goods list search (temu.local.goods.list.retrieve).
        """
        data = {
            "goodsSearchType": goods_search_type,
            "pageSize": page_size,
            "pageToken": page_token,
            "orderField": order_field,
            "orderType": order_type,
            "goodsIdList": goods_id_list,
            "outGoodsSnList": out_goods_sn_list,
            "skuIdList": sku_id_list,
            "outSkuSnList": out_sku_sn_list,
            "catIdList": cat_id_list,
            "goodsName": goods_name,
            "goodsCreateTimeFrom": goods_create_time_from,
            "goodsCreateTimeTo": goods_create_time_to,
            "goodsStatusChangeTimeFrom": goods_status_change_time_from,
            "goodsStatusChangeTimeTo": goods_status_change_time_to,
            "goodsSearchTags": goods_search_tags,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.compliance.info.fill.list.query")
    def compliance_info_fill_list_query(
        self,
        page: int,
        size: int,
        compliance_info_type: int,
        language: str = None,
        search_text: str = None,
        **kwargs
    ):
        """
        查询本地商品合规信息填写下拉列表（bg.local.goods.compliance.info.fill.list.query）。
        :param page: 页码，必填
        :param size: 每页数量，必填，最大20
        :param compliance_info_type: 查询类型，必填（如4:A/S负责人）
        :param language: 语言，选填
        :param search_text: 搜索关键字，选填
        其余参数通过 kwargs 传递。
        Query compliance information fill in the drop-down list (bg.local.goods.compliance.info.fill.list.query).
        """
        data = {
            "page": page,
            "size": size,
            "complianceInfoType": compliance_info_type,
            "language": language,
            "searchText": search_text,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.spec.id.get")
    def spec_id_get(
        self,
        cat_id: int,
        parent_spec_id: int,
        child_spec_name: str,
        **kwargs
    ):
        """
        搜索并生成商家自定义规格（bg.local.goods.spec.id.get）。
        :param cat_id: 类目ID，必填
        :param parent_spec_id: 父规格ID，必填
        :param child_spec_name: 自定义子规格名称，必填
        其余参数通过 kwargs 传递。
        Search and generate merchant-customized specifications (bg.local.goods.spec.id.get).
        """
        data = {
            "catId": cat_id,
            "parentSpecId": parent_spec_id,
            "childSpecName": child_spec_name,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.size.element.get")
    def size_element_get(
        self,
        cat_id: int,
        language: str = None,
        **kwargs
    ):
        """
        查询尺码表元素信息（bg.local.goods.size.element.get）。
        :param cat_id: 叶子类目ID，必填
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Query size chart element information (bg.local.goods.size.element.get).
        """
        data = {
            "catId": cat_id,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.cats.get")
    def cats_get(
        self,
        parent_cat_id: int,
        language: str = None,
        **kwargs
    ):
        """
        获取Temu类目（bg.local.goods.cats.get）。
        :param parent_cat_id: 父类目ID，必填（不传则查全部一级类目）
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Get Temu categories (bg.local.goods.cats.get).
        """
        data = {
            "parentCatId": parent_cat_id,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.compliance.extra.template.get")
    def compliance_extra_template_get(
        self,
        cat_id: int,
        language: str = None,
        goods_id: int = None,
        normal_property_list: list = None,
        govern_property_list: list = None,
        rep_info_list: list = None,
        **kwargs
    ):
        """
        查询必填合规信息（bg.local.goods.compliance.extra.template.get）。
        :param cat_id: 叶子类目ID，必填
        :param language: 语言，选填
        :param goods_id: 商品ID，选填
        :param normal_property_list: 普通商品属性，选填
        :param govern_property_list: 商品治理属性，选填
        :param rep_info_list: 负责人信息列表，选填
        其余参数通过 kwargs 传递。
        Inquire required compliance information (bg.local.goods.compliance.extra.template.get).
        """
        data = {
            "catId": cat_id,
            "language": language,
            "goodsId": goods_id,
            "normalPropertyList": normal_property_list,
            "governPropertyList": govern_property_list,
            "repInfoList": rep_info_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.compliance.rules.get")
    def compliance_rules_get(
        self,
        language: str = None,
        goods_id: int = None,
        cat_id: int = None,
        normal_property_list: list = None,
        govern_property_list: list = None,
        rep_info_list: list = None,
        **kwargs
    ):
        """
        查询强制资质信息（bg.local.goods.compliance.rules.get）。
        :param language: 语言，选填
        :param goods_id: 商品ID，选填，用于查询商品已填资质及图片的模板
        :param cat_id: 叶子类目ID，选填
        :param normal_property_list: 普通商品属性，选填
        :param govern_property_list: 商品治理属性，选填
        :param rep_info_list: 负责人信息列表，选填
        其余参数通过 kwargs 传递。
        Query mandatory qualification information (bg.local.goods.compliance.rules.get).
        """
        data = {
            "language": language,
            "goodsId": goods_id,
            "catId": cat_id,
            "normalPropertyList": normal_property_list,
            "governPropertyList": govern_property_list,
            "repInfoList": rep_info_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.template.get")
    def template_get(
        self,
        cat_id: int,
        language: str = None,
        goods_brand_properties: list = None,
        **kwargs
    ):
        """
        查询商品属性模板（bg.local.goods.template.get）。
        :param cat_id: 叶子类目ID，必填
        :param language: 语言，选填
        :param goods_brand_properties: 品牌属性列表，选填
        其余参数通过 kwargs 传递。
        Query product attributes template (bg.local.goods.template.get).
        """
        data = {
            "catId": cat_id,
            "language": language,
            "goodsBrandProperties": goods_brand_properties,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.brand.trademark.get")
    def brand_trademark_get(
        self,
        size: int = None,
        brand_id: int = None,
        page: int = None,
        **kwargs
    ):
        """
        查询品牌对应的商标（bg.local.goods.brand.trademark.get）。
        :param size: 每页数量，选填
        :param brand_id: 品牌ID，选填
        :param page: 页码，选填
        其余参数通过 kwargs 传递。
        Query the trademark corresponding to the brand (bg.local.goods.brand.trademark.get).
        """
        data = {
            "size": size,
            "brandId": brand_id,
            "page": page,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.gallery.signature.get")
    def gallery_signature_get(
        self,
        upload_file_type: int,
        **kwargs
    ):
        """
        获取图库上传签名（bg.local.goods.gallery.signature.get）。
        :param upload_file_type: 上传文件类型，必填（1-图片，2-视频，3-手册，4-资质文件）
        其余参数通过 kwargs 传递。
        Get gallery signature (bg.local.goods.gallery.signature.get).
        """
        data = {
            "uploadFileType": upload_file_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.compliance.property.check")
    def compliance_property_check(
        self,
        normal_property_list: list,
        **kwargs
    ):
        """
        校验商品属性设置（bg.local.goods.compliance.property.check）。
        :param normal_property_list: 普通属性列表，必填
        其余参数通过 kwargs 传递。
        Verify product attribute settings (bg.local.goods.compliance.property.check).
        """
        data = {
            "normalPropertyList": normal_property_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.stock.edit")
    def stock_edit(
        self,
        goods_id: int,
        sku_stock_target_list: list = None,
        request_unique_key: str = None,
        sku_stock_change_list: list = None,
        **kwargs
    ):
        """
        编辑商品库存（bg.local.goods.stock.edit）。
        :param goods_id: 商品ID，必填
        :param sku_stock_target_list: SKU目标库存列表，选填（全量更新）
        :param request_unique_key: 唯一请求ID，选填，防重复
        :param sku_stock_change_list: SKU库存变更列表，选填（差异更新）
        其余参数通过 kwargs 传递。
        Edit product stock with full-update and diff-update (bg.local.goods.stock.edit).
        """
        data = {
            "goodsId": goods_id,
            "skuStockTargetList": sku_stock_target_list,
            "requestUniqueKey": request_unique_key,
            "skuStockChangeList": sku_stock_change_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.list.query")
    def goods_list_query(
        self,
        page_no: int,
        page_size: int,
        goods_search_type: int,
        order_field: str = None,
        order_type: int = None,
        search_text: str = None,
        status_filter_type: int = None,
        crt_from: int = None,
        crt_to: int = None,
        goods_id_list: list = None,
        cat_id_list: list = None,
        goods_status_filter_type: int = None,
        goods_sub_status_filter_type: int = None,
        goods_status_change_time_from: int = None,
        goods_status_change_time_to: int = None,
        goods_search_tags: list = None,
        **kwargs
    ):
        """
        获取商品列表（bg.local.goods.list.query）。
        :param page_no: 页码，必填
        :param page_size: 每页数量，必填，最大100
        :param goods_search_type: 商品状态筛选，必填（1-在售/下架，4-未发布，5-草稿，6-已删除）
        :param order_field: 排序字段，选填
        :param order_type: 排序类型，选填（0-降序，1-升序）
        :param search_text: 搜索内容，选填
        :param status_filter_type: 子状态筛选类型，选填
        :param crt_from: 创建起始时间（毫秒），选填
        :param crt_to: 创建结束时间（毫秒），选填
        :param goods_id_list: 商品ID列表，选填
        :param cat_id_list: 类目ID列表，选填
        :param goods_status_filter_type: 商品状态筛选（新版本字段），选填
        :param goods_sub_status_filter_type: 商品子状态筛选（新版本字段），选填
        :param goods_status_change_time_from: 商品状态变更起始时间（毫秒），选填
        :param goods_status_change_time_to: 商品状态变更结束时间（毫秒），选填
        :param goods_search_tags: 商品搜索标签，选填
        其余参数通过 kwargs 传递。
        Get product list (bg.local.goods.list.query).
        """
        data = {
            "pageNo": page_no,
            "pageSize": page_size,
            "goodsSearchType": goods_search_type,
            "orderField": order_field,
            "orderType": order_type,
            "searchText": search_text,
            "statusFilterType": status_filter_type,
            "crtFrom": crt_from,
            "crtTo": crt_to,
            "goodsIdList": goods_id_list,
            "catIdList": cat_id_list,
            "goodsStatusFilterType": goods_status_filter_type,
            "goodsSubStatusFilterType": goods_sub_status_filter_type,
            "goodsStatusChangeTimeFrom": goods_status_change_time_from,
            "goodsStatusChangeTimeTo": goods_status_change_time_to,
            "goodsSearchTags": goods_search_tags,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.sku.list.query")
    def sku_list_query(
        self,
        sku_search_type: int,
        sku_status_filter_type: int,
        page_no: int = None,
        page_size: int = None,
        order_field: str = None,
        order_type: int = None,
        search_text: str = None,
        status_filter_type: int = None,
        crt_from: int = None,
        crt_to: int = None,
        sku_id_list: list = None,
        cat_id_list: list = None,
        sku_sub_status_filter_type: int = None,
        sku_status_change_time_from: int = None,
        sku_status_change_time_to: int = None,
        goods_search_tags: list = None,
        **kwargs
    ):
        """
        获取SKU列表及变体（bg.local.goods.sku.list.query）。
        :param sku_search_type: SKU状态，必填（2-在售，3-不可售）
        :param sku_status_filter_type: SKU状态筛选（新版本字段），必填
        :param page_no: 页码，选填
        :param page_size: 每页数量，选填，最大100
        :param order_field: 排序字段，选填
        :param order_type: 排序类型，选填（0-降序，1-升序）
        :param search_text: 搜索内容，选填
        :param status_filter_type: 子状态筛选类型，选填
        :param crt_from: 创建起始时间（毫秒），选填
        :param crt_to: 创建结束时间（毫秒），选填
        :param sku_id_list: SKU ID列表，选填
        :param cat_id_list: 类目ID列表，选填
        :param sku_sub_status_filter_type: SKU子状态筛选（新版本字段），选填
        :param sku_status_change_time_from: SKU状态变更起始时间（毫秒），选填
        :param sku_status_change_time_to: SKU状态变更结束时间（毫秒），选填
        :param goods_search_tags: 商品搜索标签，选填
        其余参数通过 kwargs 传递。
        Get sku list, as well as get Variants (bg.local.goods.sku.list.query).
        """
        data = {
            "skuSearchType": sku_search_type,
            "skuStatusFilterType": sku_status_filter_type,
            "pageNo": page_no,
            "pageSize": page_size,
            "orderField": order_field,
            "orderType": order_type,
            "searchText": search_text,
            "statusFilterType": status_filter_type,
            "crtFrom": crt_from,
            "crtTo": crt_to,
            "skuIdList": sku_id_list,
            "catIdList": cat_id_list,
            "skuSubStatusFilterType": sku_sub_status_filter_type,
            "skuStatusChangeTimeFrom": sku_status_change_time_from,
            "skuStatusChangeTimeTo": sku_status_change_time_to,
            "goodsSearchTags": goods_search_tags,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.compliance.edit")
    def compliance_edit(
        self,
        goods_id: int,
        language: str = None,
        certificate_info: dict = None,
        actual_photo: dict = None,
        rep_info: dict = None,
        extra_template: dict = None,
        **kwargs
    ):
        """
        编辑商品资质信息（bg.local.goods.compliance.edit）。
        :param goods_id: 商品ID，必填
        :param language: 语言，选填
        :param certificate_info: 资质文件，选填
        :param actual_photo: 实物照片，选填
        :param rep_info: 负责人信息，选填
        :param extra_template: 治理属性，选填
        其余参数通过 kwargs 传递。
        Edit product qualification information (bg.local.goods.compliance.edit).
        """
        data = {
            "goodsId": goods_id,
            "language": language,
            "certificateInfo": certificate_info,
            "actualPhoto": actual_photo,
            "repInfo": rep_info,
            "extraTemplate": extra_template,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.compliance.goods.list.query")
    def compliance_goods_list_query(
        self,
        page_no: int,
        page_size: int,
        search_text: str = None,
        status_list: list = None,
        optional_condition_list: list = None,
        **kwargs
    ):
        """
        商品管理属性列表查询（bg.local.compliance.goods.list.query）。
        :param page_no: 页码，必填
        :param page_size: 每页数量，必填，默认25
        :param search_text: 搜索内容，选填，支持商品名/goodsId/skuId
        :param status_list: 状态列表，选填（1-未提交，2-待审核，3-审核中，4-需处理，5-已通过，6-已驳回，7-待更新）
        :param optional_condition_list: 合规信息筛选条件，选填
        其余参数通过 kwargs 传递。
        Product management attribute list query (bg.local.compliance.goods.list.query).
        """
        data = {
            "pageNo": page_no,
            "pageSize": page_size,
            "searchText": search_text,
            "statusList": status_list,
            "optionalConditionList": optional_condition_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.category.recommend")
    def category_recommend(
        self,
        goods_name: str,
        description: str = None,
        image_url: str = None,
        expand_cat_type: int = None,
        **kwargs
    ):
        """
        根据商品名推荐类目（bg.local.goods.category.recommend）。
        :param goods_name: 商品名称，必填
        :param description: 商品描述，选填
        :param image_url: 商品图片URL，选填
        :param expand_cat_type: 扩展类目类型，选填（0-服饰，1-其他，2-图书，3-DVD，4-CD，5-种子）
        其余参数通过 kwargs 传递。
        Query recommended category by product name (bg.local.goods.category.recommend).
        """
        data = {
            "goodsName": goods_name,
            "description": description,
            "imageUrl": image_url,
            "expandCatType": expand_cat_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.property.get")
    def property_get(
        self,
        cat_id: int,
        goods_prop_list: list,
        goods_name: str,
        values: list = None,
        prop_name: str = None,
        **kwargs
    ):
        """
        获取Temu商品属性（bg.local.goods.property.get）。
        :param cat_id: 叶子类目ID，必填
        :param goods_prop_list: 商品属性列表，必填
        :param prop_name: 商品属性名（英文），选填
        其余参数通过 kwargs 传递。
        Get Temu goods attributes (bg.local.goods.property.get).
        """
        data = {
            "catId": cat_id,
            "goodsPropList": goods_prop_list,
            "propName": prop_name,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.add")
    def goods_add(
        self,
        goods_basic: dict,
        goods_service_promise: dict,
        goods_property: dict,
        sku_list: list,
        goods_origin_info: dict = None,
        bullet_points: list = None,
        goods_desc: str = None,
        certification_info: dict = None,
        guide_file_info: dict = None,
        goods_size_chart_list: dict = None,
        goods_size_image: list = None,
        goods_trademark: dict = None,
        tax_code_info: dict = None,
        goods_vehicle_property_relation: dict = None,
        second_hand: dict = None,
        **kwargs
    ):
        """
        新增商品（bg.local.goods.add）。
        :param goods_basic: 商品基础信息，必填
        :param goods_service_promise: 商家服务承诺，必填
        :param goods_property: 商品属性，必填
        :param sku_list: SKU列表，必填
        :param goods_origin_info: 原产地信息，选填
        :param bullet_points: 卖点，选填
        :param goods_desc: 商品描述，选填
        :param certification_info: 认证信息，选填
        :param guide_file_info: 说明书，选填
        :param goods_size_chart_list: 尺码表信息，选填
        :param goods_size_image: 尺码图URL，选填
        :param goods_trademark: 商标信息，选填
        :param tax_code_info: 税码信息，选填
        :param goods_vehicle_property_relation: 车辆基础数据，选填
        :param second_hand: 二手信息，选填
        其余参数通过 kwargs 传递。
        Add new items on Temu (bg.local.goods.add).
        """
        data = {
            "goodsBasic": goods_basic,
            "goodsServicePromise": goods_service_promise,
            "goodsProperty": goods_property,
            "skuList": sku_list,
            "goodsOriginInfo": goods_origin_info,
            "bulletPoints": bullet_points,
            "goodsDesc": goods_desc,
            "certificationInfo": certification_info,
            "guideFileInfo": guide_file_info,
            "goodsSizeChartList": goods_size_chart_list,
            "goodsSizeImage": goods_size_image,
            "goodsTrademark": goods_trademark,
            "taxCodeInfo": tax_code_info,
            "goodsVehiclePropertyRelation": goods_vehicle_property_relation,
            "secondHand": second_hand,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.image.upload")
    def image_upload(
        self,
        scaling_type: int = None,
        file_url: str = None,
        compression_type: int = None,
        format_conversion_type: int = None,
        **kwargs
    ):
        """
        图片素材处理（bg.local.goods.image.upload）。
        :param scaling_type: 缩放目标，选填（0-原图，1-800*800，2-1350*1800）
        :param file_url: 文件URL，选填
        :param compression_type: 压缩，选填（0-否，1-是）
        :param format_conversion_type: 格式转换，选填（0-jpg，1-jpeg，2-png）
        其余参数通过 kwargs 传递。
        Image material processing (bg.local.goods.image.upload).
        """
        data = {
            "scalingType": scaling_type,
            "fileUrl": file_url,
            "compressionType": compression_type,
            "formatConversionType": format_conversion_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.videocoverimage.get")
    def videocoverimage_get(
        self,
        vid_list: list = None,
        **kwargs
    ):
        """
        获取视频封面图（bg.local.goods.videocoverimage.get）。
        :param vid_list: 视频vid列表，选填
        其余参数通过 kwargs 传递。
        Used to obtain the cover image of the video screen (bg.local.goods.videocoverimage.get).
        """
        data = {
            "vidList": vid_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.freight.template.list.query")
    def freight_template_list_query(
        self,
        **kwargs
    ):
        """
        查询运费模板列表（bg.freight.template.list.query）。
        该接口用于商家查询运费模板列表，商品上架时可声明物流费用规则。
        其余参数通过 kwargs 传递。
        Query freight template list by Temu seller (bg.freight.template.list.query).
        """
        data = {}
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.sale.status.set")
    def sale_status_set(
        self,
        goods_id: int,
        onsale: int,
        sku_id_list: list = None,
        operation_type: int = None,
        **kwargs
    ):
        """
        商品/sku上下架操作（bg.local.goods.sale.status.set）。
        :param goods_id: 商品ID，必填
        :param onsale: 上下架状态，必填（0-下架，1-上架）
        :param sku_id_list: SKU ID列表，选填，传则只对SKU操作
        :param operation_type: 操作类型，选填（1-商品，2-SKU，null同1）
        其余参数通过 kwargs 传递。
        Support goods/SKU dimension for listing and delisting operations (bg.local.goods.sale.status.set).
        """
        data = {
            "goodsId": goods_id,
            "onsale": onsale,
            "skuIdList": sku_id_list,
            "operationType": operation_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.publish.status.get")
    def publish_status_get(
        self,
        goods_id_list: list,
        **kwargs
    ):
        """
        批量查询商品发布状态（bg.local.goods.publish.status.get）。
        :param goods_id_list: 商品ID列表，必填
        其余参数通过 kwargs 传递。
        Batch query product publication status (bg.local.goods.publish.status.get).
        """
        data = {
            "goodsIdList": goods_id_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.sku.out.sn.check")
    def sku_out_sn_check(
        self,
        out_sku_sn_list: list = None,
        language: str = None,
        **kwargs
    ):
        """
        校验SKU贡献码是否重复（bg.local.goods.sku.out.sn.check）。
        :param out_sku_sn_list: 贡献SKU编码列表，选填，最多50个，单个不超40字符
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Check if contribution ID for SKU is duplicate (bg.local.goods.sku.out.sn.check).
        """
        data = {
            "outSkuSnList": out_sku_sn_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.sku.out.sn.set")
    def sku_out_sn_set(
        self,
        modify_list: list = None,
        language: str = None,
        **kwargs
    ):
        """
        设置SKU贡献码（bg.local.goods.sku.out.sn.set）。
        :param modify_list: 贡献SKU列表，选填，单个编码不超过40字符
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Set contribution ID for SKU (bg.local.goods.sku.out.sn.set).
        """
        data = {
            "modifyList": modify_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.tax.code.get")
    def tax_code_get(
        self,
        cat_id: int = None,
        language: str = None,
        **kwargs
    ):
        """
        查询商品税码（bg.local.goods.tax.code.get）。
        :param cat_id: 叶子类目ID，选填
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        local-local goods B (bg.local.goods.tax.code.get).
        """
        data = {
            "catId": cat_id,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.out.sn.set")
    def goods_out_sn_set(
        self,
        modify_list: list = None,
        language: str = None,
        **kwargs
    ):
        """
        设置商品贡献码（bg.local.goods.out.sn.set）。
        :param modify_list: 贡献商品修改列表，选填，最多50条
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Set contribution ID for goods (bg.local.goods.out.sn.set).
        """
        data = {
            "modifyList": modify_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.out.sn.check")
    def goods_out_sn_check(
        self,
        out_goods_sn_list: list = None,
        language: str = None,
        **kwargs
    ):
        """
        校验商品贡献码是否重复（bg.local.goods.out.sn.check）。
        :param out_goods_sn_list: 贡献商品编码列表，选填，最多50条，单个不超过40字符
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Check if contribution ID for goods is repeated (bg.local.goods.out.sn.check).
        """
        data = {
            "outGoodsSnList": out_goods_sn_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.property.relations")
    def property_relations(
        self,
        relation_type: int,
        goods_id: int,
        relation_id: int,
        query_last_version: bool,
        **kwargs
    ):
        """
        查询商品关联库数据（bg.local.goods.property.relations）。
        :param relation_type: 关联类型，必填（如1-兼容车型库）
        :param goods_id: 商品ID，必填
        :param relation_id: 关联库ID，必填
        :param query_last_version: 是否查询最新版本，必填（True-最新，False-优先查活动版）
        其余参数通过 kwargs 传递。
        Query the relational database data associated with goods (bg.local.goods.property.relations).
        """
        data = {
            "relationType": relation_type,
            "goodsId": goods_id,
            "relationId": relation_id,
            "queryLastVersion": query_last_version,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.property.relations.level.template")
    def property_relations_level_template(
        self,
        cat_id: int,
        relation_type: int,
        **kwargs
    ):
        """
        获取车型库数据的分层属性值及分层ID（bg.local.goods.property.relations.level.template）。
        :param cat_id: 商品类目ID（叶子类目），必填
        :param relation_type: 关联类型，必填（如1-兼容车型库）
        其余参数通过 kwargs 传递。
        Obtaining the hierarchical attribute value and hierarchical id of vehicle type library data (bg.local.goods.property.relations.level.template).
        """
        data = {
            "catId": cat_id,
            "relationType": relation_type,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.property.relations.template")
    def property_relations_template(
        self,
        cat_id: int,
        relation_id: int,
        relation_type: int,
        property_relation_query_dto_list: list = None,
        **kwargs
    ):
        """
        通过父属性值依赖id和分层id查询全量量子属性（bg.local.goods.property.relations.template）。
        :param cat_id: 商品类目ID（叶子类目），必填
        :param relation_id: 关联id，必填
        :param relation_type: 关联类型，必填（如1-兼容车型库）
        :param property_relation_query_dto_list: 属性依赖查询DTO列表，选填
        其余参数通过 kwargs 传递。
        Query the full quantum attribute by the dependency id of the parent attribute value and the hierarchical id (bg.local.goods.property.relations.template).
        """
        data = {
            "catId": cat_id,
            "relationId": relation_id,
            "relationType": relation_type,
            "propertyRelationQueryDTOList": property_relation_query_dto_list,
        }
        return self._request(data={**data, **kwargs})

    @action("bg.local.goods.category.check")
    def category_check(
        self,
        cat_id: int = None,
        hd_thumb_url: str = None,
        carousel_image_list: list = None,
        language: str = None,
        goods_name: str = None,
        **kwargs
    ):
        """
        类目错放预检查（bg.local.goods.category.check）。
        :param cat_id: 类目ID，选填
        :param hd_thumb_url: 商品主图URL，选填
        :param carousel_image_list: 轮播图列表，选填
        :param language: 语言，选填
        :param goods_name: 商品名称，选填
        其余参数通过 kwargs 传递。
        Precheck category misplacement (bg.local.goods.category.check).
        """
        data = {
            "catId": cat_id,
            "hdThumbUrl": hd_thumb_url,
            "carouselImageList": carousel_image_list,
            "language": language,
            "goodsName": goods_name,
        }
        return self._request(data={**data, **kwargs})

    @action("temu.local.goods.spec.info.get")
    def spec_info_get(
        self,
        spec_id_list: list,
        language: str = None,
        **kwargs
    ):
        """
        查询平台规格ID对应的多语言规格值信息（temu.local.goods.spec.info.get）。
        :param spec_id_list: 规格ID列表，必填
        :param language: 语言，选填
        其余参数通过 kwargs 传递。
        Used to query the specification value information in different languages corresponding to the platform's specification ID (temu.local.goods.spec.info.get).
        """
        data = {
            "specIdList": spec_id_list,
            "language": language,
        }
        return self._request(data={**data, **kwargs})
