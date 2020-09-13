# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/13 13:03
# @Software    : PyCharm
# @Description : 剑指 Offer 47. 礼物的最大价值

'''

在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

 

示例 1:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

'''
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        xLength = len(grid)
        yLength = len(grid[0])
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(xLength):
            for j in range(yLength):
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                else:
                    if i - 1 < 0 and j - 1 < 0:
                        dp[i][j] = grid[i][j]
                        continue
                    if i - 1 < 0:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                    if j - 1 < 0:
                        dp[i][j] = dp[i - 1][j] + grid[i][j]

        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()
    grid = [[1]]
    print(so.maxValue(grid=grid))
