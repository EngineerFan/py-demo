# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/28 21:25
# @Software    : PyCharm
# @Description : 477. 汉明距离总和

from typing import List
from collections import *


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        trie = Counter()
        max_bit = len(bin(max(nums))) - 2
        ans = 0
        for i, num in enumerate(nums):
            for j in range(max_bit):
                bit = (num >> j) & 1
                if bit:
                    ans += i - trie[j]
                    trie[j] += 1
                else:
                    ans += trie[j]
        return ans


so = Solution()
nums = [4, 14, 2]

mp = Counter([0])
print('mp: ', mp)

print(so.totalHammingDistance(nums=nums))
