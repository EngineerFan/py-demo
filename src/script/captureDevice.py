# author  : Ryan
# datetime: 2020/10/15 9:33
# software: PyCharm

"""
description: 获取省区经营分析报表HTML图

"""

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1/bin/phantomjs.exe')
# driver.add_cookie({"SESSION": "3169c66a-93fd-4274-85f8-bdf9b9ab37eb"})
#
# driver.get('http://localhost:8080/report/analy/dashboard/provAnalyQty.jsp')
# print(driver.title)
# data = driver.find_element_by_id("page1").text
# print(data)
import pdfkit

pdfkit.from_url('https://www.jianshu.com', 'out.pdf')
