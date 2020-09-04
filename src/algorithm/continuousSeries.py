# author  : Ryan
# datetime: 2020/8/25 15:11
# software: PyCharm

"""
description: 17. 连续数列

给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    so = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(so.maxSubArray(nums))
