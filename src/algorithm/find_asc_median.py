# author  : Ryan
# datetime: 2020/8/5 14:08
# software: PyCharm

"""
description: 4. 寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5


"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0.0
        l1, l2 = len(num1), len(num2)
        if l1 != 0 and l2 == 0:
            print(type(l1 / 2))
            if l1 % 2 == 0:
                return (num1[int(l1 / 2)] + nums1[int(l1 / 2) - 1]) / 2
            else:
                return nums1[round(l1 / 2)]

        elif l1 == 0 and l2 != 0:
            if l2 % 2 == 0:
                return (num2[int(l2 / 2)] + nums2[int(l2 / 2) - 1]) / 2
            else:
                return num2[int(l2 / 2)]
        else:
            l1_max, l2_max = nums1[l1 - 1], nums2[l2 - 1]
            l1_min, l2_min = nums1[0], nums2[0]
            # 两种特殊情况优先解决
            if l1_min >= l2_max:
                tmp = int((l1 + l2) / 2)
                remainder = (l1 + l2) % 2
                if remainder == 0:
                    if tmp == l2:
                        return (nums2[tmp - 1] + nums1[0]) / 2
                    elif tmp < l2:
                        return (nums2[tmp - 1] + nums2[tmp - 2]) / 2
                    else:
                        tmp = tmp - l2 - 1
                        return (nums1[tmp] + nums1[tmp + 1]) / 2
                else:
                    tmp_int = round((l1 + l2) / 2)
                    if tmp_int <= l2:
                        return nums2[tmp_int - 1]
                    else:
                        tmp = tmp_int - l2
                        return nums1[tmp - 1]
            elif l2_min >= l1_max:
                tmp = int((l1 + l2) / 2)
                remainder = (l1 + l2) % 2
                if remainder == 0:
                    if tmp == l1:
                        return (nums1[tmp - 1] + nums2[0]) / 2
                    elif tmp < l1:
                        return (nums1[tmp - 1] + nums1[tmp - 2]) / 2
                    else:
                        tmp = tmp - l1 - 1
                        return (nums2[tmp] + nums2[tmp + 1]) / 2
                else:
                    tmp_int = round((l1 + l2) / 2)
                    if tmp_int <= l1:
                        return nums1[tmp_int - 1]
                    else:
                        tmp = tmp_int - l1
                        return nums2[tmp - 1]

            else:
                # 说明两个数组元素中交叉

                pass


        return median


def deep_traverse(self, nums1: List[int], nums2: List[int], mid1: int, mid2: int):
    if nums1[mid1] > nums2[mid2]:
        if mid1 == 0:
            pass
        else:
            mid1 = int(mid1 / 2)
        self.deep_traverse(nums1, nums2, mid1, mid2)
    elif nums1[mid1] < nums2[mid2]:
        pass
    else:
        pass
    pass


if __name__ == '__main__':
    so = Solution()
    num1 = [1, 3, 5]
    num2 = []
    print(so.findMedianSortedArrays(num1, num2))
