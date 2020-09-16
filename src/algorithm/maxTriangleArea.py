# author  : Ryan
# datetime: 2020/9/8 14:55
# software: PyCharm

"""
description:  最大三角形面积


给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。

"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        pass


if __name__ == '__main__':
    so = Solution()
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(so.largestTriangleArea(points))
