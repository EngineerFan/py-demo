# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/23 14:22
# @Software    : PyCharm
# @Description : 1707. 与数组中元素的最大异或值

from typing import List
from collections import *


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries_len = len(queries)
        result = []
        nums_map = Counter(nums)
        # print('nums_map: ', nums_map)
        for i in range(queries_len):
            max_res = -1
            for j in range(len(nums)):
                if nums[j] <= queries[i][1]:
                    max_res = max(queries[i][0] ^ nums[j], max_res)
            result.append(max_res)
        return result


so = Solution()
nums = [5, 2, 4, 6, 6, 3]
queries = [[12, 4], [8, 1], [6, 3]]
print(so.maximizeXor(nums, queries))
