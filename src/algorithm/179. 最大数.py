# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/4/12 10:09
# @Software    : PyCharm
# @Description : 179. 最大数


from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        len_dict = dict()
        for n in nums:
            if len_dict.get(len(str(n)), None):
                el_list = len_dict.get(len(str(n)))
                el_list.append(n)
                el_list.sort()
            else:
                len_dict[len(str(n))] = [n]
        print(len_dict)
        count = 0
        while count < len(nums):
            break

        return None


so = Solution()
print(so.largestNumber([3, 30, 34, 9, 5]))
