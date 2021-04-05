# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/4/3 22:46
# @Software    : PyCharm
# @Description : 1143. 最长公共子序列

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        M, N = len(text1), len(text2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[M][N]


so = Solution()
print(so.longestCommonSubsequence("abcde", "ace"))
