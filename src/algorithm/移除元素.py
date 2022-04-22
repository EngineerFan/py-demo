# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/16 08:29
# @Software    : PyCharm
# @Description : 移除元素

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        j = 1
        for i in range(len(nums)):
            if nums[i] != val:
                j +=1

        return j


so = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(so.removeElement(nums, val))
