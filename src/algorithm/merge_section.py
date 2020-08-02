# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/8/1 10:21
# @Software    : PyCharm
# @Description : 合并区间
from typing import List

'''
 示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge_new_list = []
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                # 如果第 i 个元素第一个元素 大于 第 j 个元素第一个元素
                if intervals[i][0] > intervals[j][0]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]

        for i in range(len(intervals)):
            if len(merge_new_list) == 0:
                merge_new_list.append(intervals[i])
            else:
                if merge_new_list[-1][-1] >= intervals[i][-1]:
                    last_merge_array = merge_new_list.pop()
                    last_merge_array = [last_merge_array[0], last_merge_array[-1]]
                    merge_new_list.append(last_merge_array)
                elif merge_new_list[-1][-1] >= intervals[i][0]:
                    last_merge_array = merge_new_list.pop()
                    last_merge_array = [last_merge_array[0], intervals[i][-1]]
                    merge_new_list.append(last_merge_array)
                else:
                    merge_new_list.append(intervals[i])
                    continue

        return merge_new_list


if __name__ == '__main__':
    so = Solution()
    array = [[1, 4], [0, 4]]
    print(so.merge(array))
