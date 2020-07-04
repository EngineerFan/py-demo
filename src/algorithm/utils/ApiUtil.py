# -*- coding: utf-8 -*-
# @Author      : Euler
# @Time        : 2020/7/4 17:00
# @Software    : PyCharm
# @Description : 获取AccessToken API


import requests
import json


def get(host, **kwargs):
    url = host + '?'
    result = ''
    for k, v in kwargs.items():
        url += k + '=' + v + '&'
    response = requests.get(url)
    if response:
        result = response.json()
        return result
    return result


def post(host, params, headers):
    result = ''
    response = requests.post(host, params, headers)
    if response:
        return response.json()
    return result


""" 自定义序列化 """


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bytes):
            return str(o, encoding='utf-8')
        return json.JSONEncoder.default(self, o)
