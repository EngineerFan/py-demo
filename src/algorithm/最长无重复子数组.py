# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/30 16:26
# @Software    : PyCharm
# @Description : 最长无重复子数组


#
#
# @param arr int整型一维数组 the array
# @return int整型
#
from collections import *


class Solution:
    def maxLength(self, arr):
        mp, res, i = {}, 0, -1
        for j in range(len(arr)):
            if arr[j] in mp:
                i = max(mp[arr[j]], i)
            mp[arr[j]] = j
            res = max(res, j - i)
        return res


so = Solution()

arr = [2, 2, 3, 4, 8, 99, 3]

print(so.maxLength(arr=arr))
