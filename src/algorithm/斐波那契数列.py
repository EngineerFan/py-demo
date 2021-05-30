# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/30 14:58
# @Software    : PyCharm
# @Description : 斐波那契数列

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[i]


so = Solution()
n = 4
print(so.Fibonacci(n=n))
