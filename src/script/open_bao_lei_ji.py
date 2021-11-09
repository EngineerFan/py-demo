# author  : Ryan
# datetime: 2021/7/8 16:42
# software: PyCharm

"""
description:

"""

from selenium import webdriver
from selenium.webdriver import ActionChains

import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://10.3.40.6/')

# 获取 “高级” 按钮
db = driver.find_element_by_id("details-button")
ActionChains(driver).move_to_element(db).click(db).perform()

# 获取不安全链接 ， 然后点击
unsafeLinkBtn = driver.find_element_by_id("proceed-link")
ActionChains(driver).move_to_element(unsafeLinkBtn).click(unsafeLinkBtn).perform()

# 输入登录账号
driver.find_element_by_id("inputUserName").send_keys(u"01990709")
# 输入登录密码
driver.find_element_by_id("inputPassword").send_keys(u"Xiaolu-2020")
# 登录操作
loginBtn = driver.find_element_by_id("loginBtn")
ActionChains(driver).move_to_element(loginBtn).click(loginBtn).perform()

# 点击表格 - 触发展开操作

time.sleep(20)
