# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/10 21:35
# @Software    : PyCharm
# @Description : 模拟POST请求


import requests
import tornado.ioloop
import tornado.web
import json
from tornado.escape import json_encode
import base64
import os

headers = {
    'Host': '49.4.92.4:8081',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept': '*/*',
    'User-Agent': 'MIT_FG/1.2.1 (iPhone; iOS 14.0; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
}

data = 'SID=8DDE2B6E-2EBC-4C24-8C67-F22F915BAACB'

account_id = '999000001343'
password = '134231'


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        """
        1 . 根据用户名账号密码，获取登陆信息
        2 . 破解验证码，模拟用户登录
        3 . 保留用户登录信息
        4 . 爬取指定列表
        """
        print(json.loads(self.request.body))
        check_code = self.get_identify_code(headers, data)
        
        resp = {'status': True, 'msg': '成功'}
        self.write(json_encode(resp))

    """
    获取登陆图片验证码
    """

    def get_identify_code(self, headers=headers, data=data):
        if os.path.exists("vcode.jpg"):
            os.remove("vcode.jpg")
        res = requests.post('http://49.4.92.4:8081/MIS-Adapter//randomAdapter', headers=headers, data=data)
        with open('vcode.jpg', 'wb') as pic:
            pic.write(res.content)
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Me6du1pWSDa0XbCjOosHc8zB&client_secret=5Whzr0t1xwNNK9KOj3ocRWxARiqPzGiF'
        response = requests.get(host)
        access_token = ''
        if response:
            data = json.loads(response.text)
            access_token = data['access_token']
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
        # 二进制方式打开图片文件
        f = open('vcode.jpg', 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + access_token
        bd_headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=bd_headers)
        check_code = ''
        if response:
            check_code = json.loads(response.text)['words_result'][0]['words']
        return check_code


def run():
    return tornado.web.Application([(r"/reptile/getData", MainHandler), ])


if __name__ == '__main__':
    app = run()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()

# cookies = {
#     'JSESSIONID': '6DF124B47464290AE71AD19271756E86',
# }
#
# headers = {
#     'Host': '49.4.92.4:8081',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
#     'Accept': '*/*',
#     'User-Agent': 'MIT_FG/1.2.1 (iPhone; iOS 14.0; Scale/2.00)',
#     'Accept-Language': 'zh-Hans-CN;q=1',
# }
#
# data = 'ADAPTER=MTXHFS1010&MODE=XS&SIGNATURE=7edb6feb-099a-4d4e-bae5-ecb99b44102b&TRADEPWD=9990000013431615382516156&TRADERID=999000001343&WAREID=900001'
#
# response = requests.post('http://49.4.92.4:8081/MIS-Adapter/xhfsAdapter.ylsoft', headers=headers, cookies=cookies,
#                          data=data)
#
# print(response.json())
