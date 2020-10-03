# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/20 10:47
# @Software    : PyCharm
# @Description : 剑指 Offer 29. 顺时针打印矩阵


"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100


"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resultList = []
        rowLength = len(matrix)
        if rowLength == 0:
            return resultList
        colLength = len(matrix[0])
        i, j = 0, 0
        while True:
            for col in range(colLength):
                resultList.append(matrix[i][col])
            pass

        return resultList
