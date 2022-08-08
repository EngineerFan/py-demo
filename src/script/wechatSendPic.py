# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/4/23 18:29
# @Software    : PyCharm
# @Description : 自动传图片到微信助手


import itchat

itchat.auto_login()
itchat.send_msg('12', toUserName='filehelper')
