# -*- coding: utf-8 -*-
import sys
from trustocean_sdk import utils
from OpenSSL import crypto


# 创建CSR和私钥
# s = utils.X509Utils()
# generate = s.generate_csr('RSA', 'www.trustocean.com', 'CN', 'Shaanxi', 'Xian', 'TrustOcean Limited', 'CyberSecurity Department')
# print(crypto.dump_certificate_request(crypto.FILETYPE_PEM, generate[0]).decode('utf-8'))
# print(crypto.dump_privatekey(crypto.FILETYPE_PEM, generate[1]).decode('utf-8'))

# 转换证书格式并创建压缩包文件
ssl_cert = """"""
ssl_key = ''''''
ssl_ca_cert = ''''''

zip_file = utils.create_certificates_zip_file(ssl_cert, ssl_key, ssl_ca_cert)
print(type(zip_file))
