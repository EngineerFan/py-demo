# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/13 10:33
# @Software    : PyCharm
# @Description : 识别


import requests
import base64
import json

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Me6du1pWSDa0XbCjOosHc8zB&client_secret=5Whzr0t1xwNNK9KOj3ocRWxARiqPzGiF'
response = requests.get(host)
access_token = ''
if response:
    data = json.loads(response.text)
    print('refresh_token: ', data['refresh_token'])
    print('access_token: ', data['access_token'])
    access_token = data['access_token']

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Me6du1pWSDa0XbCjOosHc8zB&client_secret=5Whzr0t1xwNNK9KOj3ocRWxARiqPzGiF'
# response = requests.get(host)
# access_token = ''
# if response:
#     data = json.loads(response.text)
#     print('refresh_token: ', data['refresh_token'])
#     print('access_token: ', data['access_token'])
#     access_token = data['access_token']
#
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# # 二进制方式打开图片文件
# f = open('vcode.jpg', 'rb')
# img = base64.b64encode(f.read())
# params = {"image": img}
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())
f = open('vcode.jpg', 'rb')
img = base64.b64encode(f.read())
params = {"image": img}
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())


login_host = 'http://49.4.92.4:8081/MIS-Adapter/commonAdapter'
