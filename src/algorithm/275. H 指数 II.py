# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/12 08:48
# @Software    : PyCharm
# @Description : 275. H 指数 II

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        result, left, right = 0, 0, N - 1
        if left == right and citations[right] != 0:
            return 1
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= N - mid and (mid == 0 or citations[mid - 1] <= citations[mid]):
                result = max(N - mid, result)
                right = mid
            else:
                left = mid + 1
        if left == right:
            if citations[left] >= N - left and (left == 0 or citations[left - 1] <= citations[left]):
                result = max(N - left, result)

        return result


so = Solution()
citations = [0, 1]
print(so.hIndex(citations))
