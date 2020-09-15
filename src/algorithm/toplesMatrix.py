# author  : Ryan
# datetime: 2020/9/15 8:39
# software: PyCharm

"""
description: 766. 托普利茨矩阵

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

示例 1:

输入:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。
示例 2:

输入:
matrix = [
  [1,2],
  [2,2]
]
输出: False
解释:
对角线"[1, 2]"上的元素不同。

"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rowLength = len(matrix)
        colLength = len(matrix[0])
        if rowLength == 1 or colLength == 1:
            return True
        for i in range(rowLength - 1, 0, -1):
            edgeNumber = matrix[i][0]
            m = i
            n = 0
            while m + 1 < rowLength and n + 1 < colLength:
                m, n = m + 1, n + 1
                if edgeNumber != matrix[m][n]:
                    return False
        for j in range(colLength):
            edgeNumber = matrix[0][j]
            m = 0
            n = j
            while m + 1 < rowLength and n + 1 < colLength:
                m, n = m + 1, n + 1
                if edgeNumber != matrix[m][n]:
                    return False
        return True


if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 2], [2, 2]]
    print(so.isToeplitzMatrix(matrix))
