# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/14 20:24
# @Software    : PyCharm
# @Description : 1818. 绝对差值和

from typing import List
from collections import *


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        absMap = {}
        nums1CountMap = Counter(nums1)
        print('nums1CountMap: ', nums1CountMap)
        maxIndex = -1
        maxTemp = -1
        for i in range(len(nums1)):
            absMap[i] = abs(nums1[i] - nums2[i])
            if abs(nums1[i] - nums2[i]) > maxTemp:
                maxIndex = i
                maxTemp = abs(nums1[i] - nums2[i])


        print(absMap)


so = Solution()
nums1 = [1, 10, 4, 4, 2, 7]
nums2 = [9, 3, 5, 1, 7, 4]
print(so.minAbsoluteSumDiff(nums1, nums2))
