# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/1 21:48
# @Software    : PyCharm
# @Description : 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？

from typing import *
from collections import *


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        candyTypeMaxTotalMap = {}
        candyTypeMap = {}
        init = 0
        for i in range(len(candiesCount)):
            candyTypeMap[i] = candiesCount[i]
            if i == 0:
                candyTypeMaxTotalMap[i] = candiesCount[i]
                init = candiesCount[i]
            else:
                candyTypeMaxTotalMap[i] = candiesCount[i] + init
                init = candyTypeMaxTotalMap[i]
        result = []
        for j in range(len(queries)):
            query = queries[j]
            maxTotal = candyTypeMaxTotalMap[query[0]]
            minTotal = maxTotal - candyTypeMap[query[0]] + 1
            if query[2] * (query[1] + 1) < minTotal:
                result.append(False)
            elif query[2] * (query[1] + 1) >= minTotal and query[2] * (query[1] + 1) <= maxTotal:
                result.append(True)
            elif query[2] * (query[1] + 1) > maxTotal:
                if 0 < maxTotal // (query[1] + 1) < query[2]:
                    result.append(True)
                else:
                    result.append(False)
        return result


so = Solution()
candiesCount = [7, 11, 5, 3, 8]
queries = [[2, 2, 6], [4, 2, 4], [2, 13, 1000000000]]
print(so.canEat(candiesCount=candiesCount, queries=queries))
