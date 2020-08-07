# author  : Ryan
# datetime: 2020/8/7 12:57
# software: PyCharm

"""
description: 695. 岛屿的最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

 

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。


"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = max(area, self.deepTraverse(grid, i, j))
        return area

    def deepTraverse(self, grid: List[List[int]], i, j) -> int:
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            area = 1 + self.deepTraverse(grid, i + 1, j) + self.deepTraverse(grid, i - 1, j) + self.deepTraverse(grid,
                                                                                                                 i,
                                                                                                                 j - 1) + self.deepTraverse(
                grid, i, j + 1)
            return area
        return 0


if __name__ == '__main__':
    so = Solution()
    array = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    print(so.maxAreaOfIsland(array))
