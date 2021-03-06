# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/27 20:59
# @Software    : PyCharm
# @Description : 594. 最长和谐子序列

"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        maxVal = 0
        length = len(nums)
        for i in range(length):
            remain = length - (i + 1)
            equCount, addCount = 0, 0
            for j in range(i + 1, length):
                if nums[j] - nums[i] == 0:
                    equCount += 1
                elif nums[j] - nums[i] == 1:
                    addCount += 1


if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    print(so.findLHS(nums))
