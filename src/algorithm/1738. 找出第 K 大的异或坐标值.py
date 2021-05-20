# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/5/19 20:02
# @Software    : PyCharm
# @Description : 1738. 找出第 K 大的异或坐标值

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        K_arr = []
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                K_arr.append(dp[i][j])
        print('dp: ', dp)
        K_arr.sort()
        print(K_arr)
        return K_arr[len(K_arr) - k]


so = Solution()
print(so.kthLargestValue([[10, 9, 5], [2, 0, 4], [1, 0, 9], [3, 4, 8]], 10))
