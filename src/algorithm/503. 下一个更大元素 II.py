# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/3/6 13:37
# @Software    : PyCharm
# @Description : 503. 下一个更大元素 II
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        is_found = False
        for i in range(length):
            for m in range(i + 1, length):
                if nums[m] > nums[i]:
                    result.append(nums[m])
                    is_found = True
                    break
            if not is_found:
                for n in range(i):
                    if nums[n] > nums[i]:
                        result.append(nums[n])
                        is_found = True
                        break
            if not is_found:
                result.append(-1)
            is_found = False

        return result


s = Solution()
print(s.nextGreaterElements(nums=[1, 2, 1]))
