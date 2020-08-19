# author  : Ryan
# datetime: 2020/8/18 17:14
# software: PyCharm

"""
description: 118. 杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            if i == 1:
                result.append([1])
                continue
            if i == 2:
                result.append([1, 1])
                continue
            prevList = result[i - 2]
            nowList = [1]
            for j in range(i - 2):
                element = prevList[j] + prevList[j + 1]
                nowList.append(element)
            nowList.append(1)
            result.append(nowList)
        return result


if __name__ == '__main__':
    s = Solution()
    numRows = 5
    print(s.generate(numRows))
