# author  : Ryan
# datetime: 2020/8/18 9:17
# software: PyCharm

"""
description: 88. 合并两个有序数组



给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。



说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m != 0 and n != 0 and nums2[0] >= nums1[-1]:
            nums1 = nums1 + nums2
        if m != 0 and n != 0 and nums2[-1] <= nums1[0]:
            nums1 = nums2 + nums1
        for i in range(m):
            k = i + 1
            for j in range(n):
                if nums1[i] <= nums2[j] <= nums1[k]:
                    nums1.insert(i, nums2[j])

        print(nums1)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    n = 3
    m = 3
    print(s.merge(nums1, m, nums2, n))
