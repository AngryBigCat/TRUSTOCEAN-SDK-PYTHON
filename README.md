## TRUSTOCEAN SSL SDK
由TrustOcean Limited专门为Python用户开发的TrustOcean API SDK, 用于对接数字证书接口，支持数字证书申请、吊销、验证、续期等操作。

### 安装步骤
1.确保Python版本正确：
- Python >= 3.6

2.安装依赖库
```python
pip install request
pip install pyOpenSSL
```

3.安装此SDK
```python
pip install trustocean_sdk
```

### 开始使用
在开始使用此API SDK库之前，请确保您已经拥有了环智中诚的账户，且保证您的账户已经具备了API服务的访问权限。
- 如果还没有账户？[访问此注册账户](https://console.trustocean.com/)
- 还没有API访问权限？[访问此申请通用的API权限](https://trustocean.com/partner-program)

#### 获取API登陆信息并添加白名单
- API USERNAME就是您的环智中诚账户邮箱地址/Tier2 API的用户名
- API PASSWORD/Token密码,如果您已经生成过，请继续使用之前生成的。如果还没有生成，可以通过 [访问此页面创建](https://console.trustocean.com/partner/api-setting) ，特别注意，当您生成了新的API-Token之后，之前的API-Token将会失效。
- 同时需要将您用于请求API的电脑/服务器的公网IPv4地址添加到 [此页面的API白名单](https://console.trustocean.com/partner/api-setting) 一栏，才可确保能正常和接口交互。

