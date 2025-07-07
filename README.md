# temu_api
temu 开发者sdk temu api
```shell
pip install temu_api
```

## 模块说明


### 1. Auth 认证模块

```python
from temu_api import TemuClient

APP_KEY = 'your_app_key'
APP_SECRET = 'your_app_secret'
ACCESS_TOKEN = 'your_access_token'
BASE_URL = 'https://openapi-b-us.temu.com'

temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)

# 获取当前 access_token 的权限信息
res = temu_client.auth.get_access_token_info()
print(res)

# 创建 access_token（授权回调）
res = temu_client.auth.create_access_token_info()
print(res)
```
- `get_access_token_info(**kwargs)`：获取当前 access_token 的 API 权限列表。
- `create_access_token_info(**kwargs)`：通过授权回调获取 access_token。

### 2. Order 订单模块

```python
from temu_api import TemuClient

APP_KEY = 'your_app_key'
APP_SECRET = 'your_app_secret'
ACCESS_TOKEN = 'your_access_token'
BASE_URL = 'https://openapi-b-us.temu.com'

temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)

# 批量获取订单列表
res = temu_client.order.list_orders_v2()
print('list_orders_v2', res)

# 获取订单详情
res = temu_client.order.detail_order_v2(parent_order_sn='PO-211-00822146499192890')
print('detail_order_v2', res)

# 获取订单收货地址
res = temu_client.order.shippinginfo_order_v2(parent_order_sn='PO-211-00822146499192890')
print('shippinginfo_order_v2', res)

# 获取可合并发货的父订单分组
res = temu_client.order.combinedshipment_list_order()
print('combinedshipment_list_order', res)

# 批量获取订单定制商品内容
res = temu_client.order.customization_order(order_sn_list=['xxx', 'yyy'])
print('customization_order', res)

# 获取订单敏感收货地址
res = temu_client.order.decryptshippinginfo_order(parent_order_sn='PO-211-20063653668472890')
print('decryptshippinginfo_order', res)
```
- `list_orders_v2(...)`：批量获取订单列表，支持多种筛选参数。
- `detail_order_v2(parent_order_sn, ...)`：获取指定父订单的详细信息。
- `shippinginfo_order_v2(parent_order_sn, ...)`：获取指定父订单的收货地址信息。
- `combinedshipment_list_order(...)`：获取可合并发货的父订单分组。
- `customization_order(order_sn_list, ...)`：批量获取订单定制商品内容信息。
- `decryptshippinginfo_order(parent_order_sn, ...)`：获取指定父订单的敏感收货地址信息。

---

如需更多用法和参数说明，请参考源码注释。

## 测试用例说明

本项目自带简单的接口测试用例，位于 tests 目录下。

### 运行测试

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行测试脚本（以 auth 和 order 为例）：
```bash
python tests/test_auth.py
python tests/test_order.py
```

### tests/test_auth.py 示例
```python
from temu_api import TemuClient

temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
res = temu_client.auth.get_access_token_info()
print(res)
res = temu_client.auth.create_access_token_info()
print(res)
```

### tests/test_order.py 示例
```python
from temu_api import TemuClient

temu_client = TemuClient(APP_KEY, APP_SECRET, ACCESS_TOKEN, BASE_URL)
res = temu_client.order.list_orders_v2()
# 写入 json 文件
import json
with open('order_list.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)
print(res)
# 其它接口调用见源码
```

如需自定义参数或更多接口测试，请参考 tests 目录下的源码。
