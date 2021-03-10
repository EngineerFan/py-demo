# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/10 21:35
# @Software    : PyCharm
# @Description : 模拟POST请求


import requests

cookies = {
    'JSESSIONID': '6DF124B47464290AE71AD19271756E86',
}

headers = {
    'Host': '49.4.92.4:8081',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept': '*/*',
    'User-Agent': 'MIT_FG/1.2.1 (iPhone; iOS 14.0; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
}

data = 'ADAPTER=MTXHFS1010&MODE=XS&SIGNATURE=7edb6feb-099a-4d4e-bae5-ecb99b44102b&TRADEPWD=9990000013431615382516156&TRADERID=999000001343&WAREID=900001'

response = requests.post('http://49.4.92.4:8081/MIS-Adapter/xhfsAdapter.ylsoft', headers=headers, cookies=cookies, data=data)

print(response.json())