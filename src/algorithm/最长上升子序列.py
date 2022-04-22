# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/28 21:40
# @Software    : PyCharm
# @Description : 最长上升子序列

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > max(nums[:i]):
                dp[i] = max(dp[:i]) + 1
            else:
                dp[i] = dp[i - 1]
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
