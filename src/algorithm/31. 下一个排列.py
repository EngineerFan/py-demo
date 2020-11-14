# author  : Ryan
# datetime: 2020/11/10 8:44
# software: PyCharm

"""
description: 31. 下一个排列

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if i - 1 != -1 and nums[i] > nums[i - 1]:
                try:
                    minNumber = min([number for number in nums[:]])
                    index = nums.index(i, minNumber)
                except ValueError:
                    index = -2
                nums[index], nums[i - 1] = nums[i - 1], nums[index]
                for j in range(i, length):
                    for k in range(j + 1, length):
                        if nums[j] > nums[k]:
                            nums[j], nums[k] = nums[k], nums[j]
                # nums[i:].sort(reverse=False)
                break
            if i == 0:
                nums.sort(reverse=False)


if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, 2]
    so.nextPermutation(nums)
    print(nums)
