# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/20 18:44
# @Software    : PyCharm
# @Description : 692. 前K个高频单词


from collections import *
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        l = Counter(words)
        inverse_map = {}
        for m, n in l.items():
            inverse_map[n] = inverse_map.get(n, [])
            inverse_map[n].append(m)

        sorted(inverse_map.keys(), reverse=True)
        result = []
        for m, n in inverse_map.items():
            freq = len(inverse_map.get(m))
            if freq <= k:
                result = result + sorted(inverse_map.get(m))
                k = k - freq
            else:
                temp = sorted(inverse_map.get(m))
                for i in range(0, k):
                    result.append(temp[i])
                break
        return result


so = Solution()
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(so.topKFrequent(words=words, k=k))
