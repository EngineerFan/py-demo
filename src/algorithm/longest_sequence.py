# author  : Ryan
# datetime: 2020/7/27 14:13
# software: PyCharm

"""
description: 最长子序列

"""

from typing import List


class Solution:

    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
        max_val = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_val = max(max_val, dp[i][j])
        return max_val


if __name__ == '__main__':
    solu = Solution()
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    max_val = solu.findLength(A, B)
    print(max_val)
