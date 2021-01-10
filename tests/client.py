# -*- coding: utf-8 -*-
from trustocean_sdk import client
import json

# 初始化API客户端实例
apiClient = client.APIClient("<your api username>", '<your api password here>')

# 检查API服务的可用状态
# response = apiClient.check_service_status()

# 获取账户基本信息
# response = apiClient.get_account_info()

# 获取账户内可订购的产品和定价信息
# response = apiClient.get_product_list()

# ping API服务是否正常
response = apiClient.get_product_list_with_pricing()

# 检查本地生成的unique_id是否可用
# response = apiClient.check_unique_id('sometestunique2200')
print(response)
