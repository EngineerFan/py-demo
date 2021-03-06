# author  : Ryan
# datetime: 2020/9/9 13:55
# software: PyCharm

"""
description: 746. 使用最小花费爬楼梯


数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0 for i in range(length)]
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, length):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        print(dp)
        return min(dp[-2], dp[-1])


if __name__ == '__main__':
    so = Solution()
    cost = [0, 1, 2, 2]
    print(so.minCostClimbingStairs(cost))
