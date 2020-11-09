# author  : Ryan
# datetime: 2020/11/9 16:58
# software: PyCharm

"""
description: 973. 最接近原点的 K 个点

我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

 

示例 1：

输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
示例 2：

输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
 

提示：

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        resultList = []
        resultDict = {}
        for i in range(len(points)):
            key = pow(pow(points[i][0], 2) + pow(points[i][1], 2), 0.5)
            resultList.append(key)
            if resultDict.get(key, None) is None:
                resultDict[key] = [points[i]]
            else:
                tempList = resultDict.get(key)
                tempList.append(points[i])
                resultDict[key] = tempList

        resultList = sorted(resultList)
        result = []
        i = 0
        while i < K:
            temp = resultDict.get(resultList[i], None)
            result.append(temp[0])
            temp.pop(0)
            if len(temp) != 0:
                resultDict[resultList[i]] = temp
            i = i + 1
        return result


if __name__ == '__main__':
    so = Solution()
    # points = [[3, 3], [5, -1], [-2, 4]]
    points = [[1, 3], [-2, 2]]
    K = 1
    print(so.kClosest(points=points, K=K))
