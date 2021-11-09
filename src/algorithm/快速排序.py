# author  : Ryan
# datetime: 2021/11/9 21:19
# software: PyCharm

"""
description:

"""
from typing import List


class Solution:

    def quick_sort(self, nums: List[int], left: int, right: int) -> None:
        if left < right:
            q = self.partition(nums, left, right)
            self.quick_sort(nums, left, q - 1)
            self.quick_sort(nums, q + 1, right)
        print(nums)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1


if __name__ == '__main__':
    so = Solution()
    nums = [1, 3, 5, 2, 86, 23, 11, 54, 22, -23, 33]
    print(so.quick_sort(nums, 0, len(nums) - 1))
