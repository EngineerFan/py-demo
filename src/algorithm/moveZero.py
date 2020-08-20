# author  : Ryan
# datetime: 2020/8/19 16:58
# software: PyCharm

"""
description: 283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i, k = 0, 0
        while i < length:
            if nums[i] == 0:
                k = k + 1
                i = i + 1
                continue
            if k > 0 and i - k >= 0:
                nums[i], nums[i - k] = nums[i - k], nums[i]
            i = i + 1
        print(nums)


if __name__ == '__main__':
    so = Solution()
    nums = [0, 1, 0, 3, 12]
    print(so.moveZeroes(nums))
