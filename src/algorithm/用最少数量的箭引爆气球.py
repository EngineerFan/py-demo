# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/14 21:54
# @Software    : PyCharm
# @Description : 用最少数量的箭引爆气球


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        y0 = points[0][1]
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > y0:
                result += 1
                y0 = points[i][1]
        return result


so = Solution()
points = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(so.findMinArrowShots(points))
