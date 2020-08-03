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
from typing import List
import time


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start = time.time()
        result = []
        count_dic = {}
        nums_length = len(nums)
        for i in range(nums_length):
            if count_dic[str(nums[i])] is None:
                count_dic[str(nums[i])] = 1
            else:
                continue
            for j in range(i + 1, nums_length):
                a, b = nums[i], nums[j]
                c = -(a + b)
                if c in nums:
                    c_index = nums.index(c)
                    if c_index == i or c_index == j:
                        continue
                    s_l = set([a, b, c])
                    flag = False
                    for li in result:
                        if set(li) == s_l:
                            flag = True
                            break
                    if not flag:
                        result.append([a, b, c])
        end = time.time()
        print('s: ', (end - start))
        return result


if __name__ == '__main__':
    so = Solution()
    array = [-1, 0, 1, 2, -1, -4]

    print(so.threeSum(array))
