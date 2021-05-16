# author  : Ryan
# datetime: 2021/5/16 20:29
# software: PyCharm

"""
description: 421. 数组中两个数的最大异或值

"""
from typing import List


class Trie:

    def __init__(self, val):
        self.val = val
        self.child = {}



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        length = len(format(max(nums), 'b')) - 1

        root = Trie(-1)

        for n in nums:
            current = root
            for i in range(length, -1, -1):
                v = (n >> i) & 1
                if v not in current.child:
                    current.child[v] = Trie(v)
                current = current.child[v]

        res = 0

        print('root: ', root)

        for n in nums:
            current = root
            total = 0
            for i in range(length, -1, -1):
                v = (n >> i) & 1
                if 1 - v in current.child:
                    total = total * 2 + 1
                    current = current.child[1 - v]
                else:
                    total = total * 2
                    current = current.child[v]
            res = max(res, total)
        return res


s = Solution()
print(s.findMaximumXOR([8, 10, 2]))
