# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/4/10 22:44
# @Software    : PyCharm
# @Description : 2021 - 4.10 commemoration day

from datetime import datetime


current = datetime.strptime('2021-04-10', '%Y-%m-%d')
start = datetime.strptime('2021-01-01', '%Y-%m-%d')

diff = current.__sub__(start)
print(diff.days + 1)
