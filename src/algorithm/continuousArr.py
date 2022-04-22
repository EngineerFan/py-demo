# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/3 19:33
# @Software    : PyCharm
# @Description : 最长连续子数组

from typing import List
from collections import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}
        count = result = 0
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            if count in mp:
                result = max(result, i - mp[count])
            else:
                mp[count] = i
        return result


nums = [0, 1, 0, 1, 1]

so = Solution()
print(so.findMaxLength(nums))
