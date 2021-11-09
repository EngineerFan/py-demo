# author  : Ryan
# datetime: 2020/9/17 20:07
# software: PyCharm

"""
description:

"""
from typing import List


def sortColors(nums: List[int]) -> List[int]:
    zero, i = 0, 0
    two = len(nums)
    while i < two:
        if nums[i] == 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            i += 1
            zero += 1
        elif nums[i] == 1:
            i += 1
        else:
            two -= 1
            nums[i], nums[two] = nums[two], nums[i]
    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))
