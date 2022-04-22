# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/14 11:02
# @Software    : PyCharm
# @Description : 登陆接口模拟


import requests
import json

import requests
import json
import base64

headers = {
    'Host': '49.4.92.4:8081',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept': '*/*',
    'User-Agent': 'MIT_FG/1.2.1 (iPhone; iOS 14.0; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
}

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Me6du1pWSDa0XbCjOosHc8zB&client_secret=5Whzr0t1xwNNK9KOj3ocRWxARiqPzGiF'
response = requests.get(host)
access_token = ''
if response:
    data = json.loads(response.text)
    print('refresh_token: ', data['refresh_token'])
    print('access_token: ', data['access_token'])
    access_token = data['access_token']

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('vcode.jpg', 'rb')
img = base64.b64encode(f.read())
params = {"image": img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())


data = 'encrypt_data=7xIOdJH6S6O5D8g9qbOLY%2BqDQPAWY4vhtASBn7wGnsLrpPOy81B%2FiWybGZNOzM2FA9ZkkonlfkWRduQDygar7XzvcN3SudJ2lYMsiShZta1dyAfo7qdOp3ahKR8tCm73IWMZxILfSqOc9wOCXzgc5kTzDslai57%2FZEDWFWTajLAWebLjx0S%2F%2F8SF%2F8fxKdTN%2FgFJi5%2Bu2epZtXsqG143pu4TS0P%2F6eKwpy9zDfiGoBA%3D&encrypt_key=03e33700c34d6295412e4284ca097e301531a6dc8479848f349fbf8fac22beadaa7d2c1ba687f0a3018e227c48ed353a66e75f5123ea89336f3d5ff2010dc45d9ade120b42096ed4fb95430bcf47b957b23b0c5e29c16345345187cd0d67c206c4cdd6ab5c3291090edce5d1e4541dfb91c6a205edc4db3f5b96bee19eb5e37d'

response = requests.post('http://49.4.92.4:8081/MIS-Adapter/commonAdapter', headers=headers, data=data)

print(json.loads(response.text))
