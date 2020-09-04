# author  : Ryan
# datetime: 2020/9/4 9:03
# software: PyCharm

"""
description: 896. 单调数列

如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。

 

示例 1：

输入：[1,2,2,3]
输出：true
示例 2：

输入：[6,5,4,4]
输出：true
示例 3：

输入：[1,3,2]
输出：false
示例 4：

输入：[1,2,4,5]
输出：true
示例 5：

输入：[1,1,1]
输出：true

"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        length = len(A)
        flag = None
        for i in range(length):
            if i != 0 and A[i] == A[i - 1]:
                continue
            elif i != 0 and A[i] > A[i - 1]:
                if flag is None:
                    flag = -1
                elif flag == -1:
                    continue
                else:
                    return False
            elif i != 0 and A[i] < A[i - 1]:
                if flag is None:
                    flag = 1
                elif flag == 1:
                    continue
                else:
                    return False
            else:
                continue

        return True
