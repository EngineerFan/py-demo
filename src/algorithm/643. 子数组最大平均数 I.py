# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/29 21:43
# @Software    : PyCharm
# @Description : 643. 子数组最大平均数 I

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        length = len(nums)
        first = sum(nums[0:k])
        maxVal = first
        for i in range(1, length):
            if i + k - 1 >= length:
                break
            first = first + nums[i + k - 1] - nums[i - 1]
            maxVal = max(maxVal, first)
        return maxVal / k


if __name__ == '__main__':
    so = Solution()
    nums = [0, 4, 0, 3, 2]
    k = 1
    print(so.findMaxAverage(nums, k))
