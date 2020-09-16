# author  : Ryan
# datetime: 2020/8/20 20:37
# software: PyCharm

"""
description: 16.06. 最小差

给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
输出： 3，即数值对(11, 8)
提示：

1 <= a.length, b.length <= 100000
-2147483648 <= a[i], b[i] <= 2147483647
正确结果在区间[-2147483648, 2147483647]内

"""

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        pass


if __name__ == '__main__':
    so = Solution()
    a = [1, 3, 15, 11, 2]
    b = [23, 127, 235, 19, 8]
    print(so.smallestDifference(a, b))
