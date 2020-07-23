# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/10 16:29
# @Software    : PyCharm
# @Description : 网页刷新

import sys

s0 = set([0, 1, 2, 3, 4])
s1 = set([2, 3])
s2 = set([3, 4])

result = s0 - (s1 | s2)
print(result)

node_list = list(range(0, 5))
print(node_list)
