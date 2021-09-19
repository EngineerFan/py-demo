# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/6 16:38
# @Software    : PyCharm
# @Description : 474. 一和零

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, length + 1):
            zeroOneArr = self.countZeroOneArr(strs[i - 1])
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    zeros = zeroOneArr[0]
                    ones = zeroOneArr[1]
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
        return dp[length][m][n]

    def countZeroOneArr(self, string: str):
        zeroOneArr = [0, 0]
        for s in string:
            zeroOneArr[int(s)] += 1
        return zeroOneArr


so = Solution()
strings = ["10", "0", "1"]
m = 1
n = 1
print(so.findMaxForm(strings, m, n))
