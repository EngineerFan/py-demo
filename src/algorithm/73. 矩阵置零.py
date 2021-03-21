# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/21 21:39
# @Software    : PyCharm
# @Description : 73. 矩阵置零

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        position_list = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    position_list.append((i, j))
        for t in position_list:
            for i in range(len(matrix[0])):
                matrix[t[0]][i] = 0
            for j in range(len(matrix)):
                matrix[j][t[1]] = 0
        return matrix


so = Solution()
print(so.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
