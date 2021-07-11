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
        if N == 0:
            return 0
        if N == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
        citations.sort()
        c = collections.Counter(citations)
        result = 0
        if result == 0 and N == c[result]:
            return result
        for i in range(N):
            if (i == 0 and citations[i] >= N - i) or (citations[i] >= N - i and citations[i - 1] < citations[i]) or (
                    citations[i] >= N - i and citations[i - 1] == citations[i]):
                result = max(N - i, result)
        return result


so = Solution()
citations = [2, 2, 2]
print(so.hIndex(citations))
