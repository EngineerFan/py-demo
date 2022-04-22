# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/27 14:25
# @Software    : PyCharm
# @Description : 213. 打家劫舍 II

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        dp = [0] * (length + 1)
        dp[0], dp[1] = 0, nums[0]
        for i in range(2, length):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        a = dp[length - 1]
        dp[1], dp[2] = 0, nums[1]
        for j in range(3, length + 1):
            dp[j] = max(dp[j - 2] + nums[j - 1], dp[j - 1])
        b = dp[length]
        return max(a, b)


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3]
    print(so.rob(nums))
