# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/11/10 22:42
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        print(f)


if __name__ == '__main__':
    so = Solution()
    m = 3
    n = 4
    print(so.uniquePaths(m, n))
