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
        init = 0
        for i in range(len(candiesCount)):
            if i == 0:
                candyTypeMaxTotalMap[i] = candiesCount[i]
                init = candiesCount[i]
            else:
                candyTypeMaxTotalMap[i] = candiesCount[i] + init
                init = candyTypeMaxTotalMap[i]
        print(candyTypeMaxTotalMap)



so = Solution()
candiesCount = [7, 4, 5, 3, 8]
queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
so.canEat(candiesCount=candiesCount, queries=queries)
