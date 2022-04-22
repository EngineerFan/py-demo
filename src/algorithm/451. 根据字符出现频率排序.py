# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/3 09:23
# @Software    : PyCharm
# @Description : 451. 根据字符出现频率排序

from collections import *


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(list(s))
        result = ''
        for k, v in c.most_common():
            result += k * v
        return result


so = Solution()
s = 'tree'
print(so.frequencySort(s))
