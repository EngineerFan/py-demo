# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/29 08:41
# @Software    : PyCharm
# @Description : 168. Excel表列名称

from collections import *


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            result.append(chr(a0 - 1 + ord('A')))
            columnNumber = (columnNumber - a0) // 26
        return "".join(result[::-1])


so = Solution()
# print(so.convertToTitle(2147483647))
print(so.convertToTitle(701))
