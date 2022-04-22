# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/3 14:16
# @Software    : PyCharm
# @Description : 746. 使用最小花费爬楼梯

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 2:
            return min(cost[0], cost[1])
        result = [0 for _ in range(length + 1)]
        result[0], result[1] = cost[0], cost[1]
        for i in range(2, length + 1):
            if i == length:
                result[i] = min(result[i - 2], result[i - 1] + cost[i - 1])
            else:
                result[i] = min(result[i - 2], result[i - 1]) + cost[i]
        print(result)
        return min(result[length], result[length - 1])


so = Solution()
cost = [10, 15, 20]
print(so.minCostClimbingStairs(cost))
