# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/23 11:10
# @Software    : PyCharm
# @Description : 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。

from typing import List, Dict
import numpy as np


class Solution:
    """
    输入:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        path = [([0] * col) for i in range(row)]
        # print(path)
        path[0][0] = grid[0][0]
        for i in range(1, row):
            path[i][0] = path[i - 1][0] + grid[i][0]
        for j in range(1, col):
            path[0][j] = path[0][j - 1] + grid[0][j]
        for r in range(1, row):
            for c in range(1, col):
                path[r][c] = min(path[r - 1][c], path[r][c - 1]) + grid[r][c]
        # print(path)
        return path[row - 1][col - 1]


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(solution.minPathSum(matrix))
