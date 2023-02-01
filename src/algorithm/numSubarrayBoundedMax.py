from typing import *

'''
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。

生成的测试用例保证结果符合 32-bit 整数范围。

'''


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result = 0
        point2 = point1 = -1
        for i, e in enumerate(nums):
            if left <= e <= right:
                point1 = i
            elif e > right:
                point2 = i
                point1 = -1
            if point1 != -1:
                result += point1 - point2
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.numSubarrayBoundedMax(nums=[2, 9, 2, 5, 6], left=2, right=8))
