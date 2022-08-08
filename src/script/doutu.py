# author  : Ryan
# datetime: 2022/4/20 16:53
# software: PyCharm

"""
description:

"""

# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import time
import urllib


class doutuSpider(object):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}

    def get_url(self, url):
        data = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(data.content, 'lxml')
        totals = soup.findAll("a", attrs={"class": "col-sm-3"})
        path = '/Users/fxl/Documents/doutu'
        folder = time.strftime("%Y%m%d", time.localtime())
        if not os.path.exists(path + '/' + folder):
            os.makedirs(path + '/' + folder)
        for a in totals:
            aTag = a.children
            for t in aTag:
                urlStr = t.get('src')
                print(urlStr)
                response = requests.get(urlStr)
                filename = os.path.basename(urlStr)
                img = response.content
                try:
                    if not os.path.exists(path + '/' + folder + '/' + filename):
                        with open(path + '/' + folder + '/' + filename, 'wb') as f:
                            f.write(img)
                except Exception as ex:
                    print(ex)
            time.sleep(10)

        pass

    def create(self):
        for count in range(1, 2):
            url = 'http://www.adoutu.com/picture/list/{}'.format(count)
        # print('开始下载第{}页'.format(cou¬nt))
        self.get_url(url)


if __name__ == '__main__':
    doutu = doutuSpider()
    doutu.create()
