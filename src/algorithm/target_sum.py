# author  : Ryan
# datetime: 2020/7/28 14:15
# software: PyCharm

"""
description: 目标和

"""

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        target_sum = 0
        for num in nums:
            target_sum = target_sum + num
        if target_sum < S or (target_sum + S) % 2 == 1:
            return 0
        return self.subsets(nums, int((target_sum + S) / 2))

    def subsets(self, nums: List[int], target_S) -> int:
        n = len(nums)
        dp = [[0 for i in range(target_S + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(target_S + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target_S]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    S = 3
    so = Solution()
    result = so.findTargetSumWays(nums, S)
    print(result)
