# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/16 14:33
# @Software    : PyCharm
# @Description : 1846. 减小和重新排列数组后的最大元素

from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        arr.sort()
        for i in range(len(arr)):
            if i != 0 and arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1
            elif i == 0 and arr[i] != 1:
                arr[i] = 1
            else:
                pass

        return arr[-1]


so = Solution()
arr = [73, 98, 9]
print(so.maximumElementAfterDecrementingAndRearranging(arr))
