# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/2 20:31
# @Software    : PyCharm
# @Description :

from typing import List
from collections import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        surplus = [i % k for i in nums]
        pre_sum = [surplus[0]]
        seen = {surplus[0]: 0}
        for i in range(1, len(surplus)):
            s = (pre_sum[-1] + surplus[i]) % k
            if s == 0 or (s in seen and i - seen[s] > 1):
                return True
            if s not in seen:
                seen[s] = i
            pre_sum.append(s)
        return False


so = Solution()
nums = [0, 0]
k = 1
print(so.checkSubarraySum(nums=nums, k=k))
