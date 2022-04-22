# author  : Ryan
# datetime: 2021/11/24 19:37
# software: PyCharm

"""
description:

"""
from typing import List


class Lad:

    def longArrayDivide(self, array: List[int], low: int, mid: int, high: int) -> int:
        lef_sum = float('-inf')
        seq_sum = 0
        max_left = -1
        for i in range(mid, low, -1):
            seq_sum = seq_sum + array[i]
            if seq_sum > lef_sum:
                lef_sum = seq_sum
                max_left = i
        rig_sum = float('-inf')
        seq_r_sum = 0
        max_right = -1
        for j in range(mid + 1, high):
            seq_r_sum = seq_r_sum + array[j]
            if seq_r_sum > rig_sum:
                rig_sum = seq_r_sum
                max_right = j
        return (max_left, max_right), lef_sum + rig_sum


if __name__ == '__main__':
    lad = Lad()
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, mid, high = 0, len(array) // 2, len(array) - 1
    print(lad.longArrayDivide(array, low, mid, high))
