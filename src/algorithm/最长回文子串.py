# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/1 13:44
# @Software    : PyCharm
# @Description :


# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def getLongestPalindrome(self, A, n):
        if n <= 1:
            return n
        dp = [[False for _ in range(n)] for _ in range(n)]
        result = 0
        A_list = list(A)
        for r in range(n):
            for l in range(r + 1):
                if r - l < 2:
                    dp[l][r] = A_list[l] == A_list[r]
                else:
                    dp[l][r] = dp[l + 1][r - 1] and A_list[l] == A_list[r]
                if dp[l][r]:
                    result = max(result, r - l + 1)
        print(np.array(dp))
        return result


so = Solution()
A = "aabba"
n = 5
print(so.getLongestPalindrome(A=A, n=n))
