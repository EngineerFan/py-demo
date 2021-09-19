# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/16 19:38
# @Software    : PyCharm
# @Description : 删除排序数组中的重复项 II

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        j = 1
        tmp = 0
        for i in range(1, length):
            if i - tmp >= 2 and nums[i] == nums[tmp]:
                continue
            else:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j


so = Solution()
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(so.removeDuplicates(nums))
