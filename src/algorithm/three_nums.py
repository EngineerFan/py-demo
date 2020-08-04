# author  : Ryan
# datetime: 2020/7/31 13:42
# software: PyCharm

"""
description: 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
import time
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=False)
        print(nums)
        result = []

        nums_length = len(nums)
        print('num_length: ', nums_length)
        for i in range(nums_length - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            a = i
            b = i + 1
            c = nums_length - 1
            sum_a = 0 - nums[a]
            while b < c:
                if c < nums_length - 1 and nums[c] == nums[c + 1]:
                    c = c - 1
                    continue
                if nums[b] + nums[c] > sum_a:
                    c = c - 1
                elif nums[b] + nums[c] < sum_a:
                    b = b + 1
                else:
                    result.append([nums[a], nums[b], nums[c]])
                    b = b + 1
                    c = c - 1
        return result


if __name__ == '__main__':
    so = Solution()
    array = [1, -1, -1, 0]

    print(so.threeSum(array))
