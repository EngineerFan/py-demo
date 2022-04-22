# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/11 13:21
# @Software    : PyCharm
# @Description : 274. H 指数
from typing import List
import collections


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        result = 0
        for i in range(N):
            if citations[i] >= N - i and (i == 0 or citations[i - 1] <= citations[i]):
                result = max(N - i, result)
        return result


so = Solution()
citations = [0]
print(so.hIndex(citations))
