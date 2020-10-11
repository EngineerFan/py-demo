# author  : Ryan
# datetime: 2020/10/9 13:46
# software: PyCharm

"""
description: 326. 3的幂


给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false

"""

from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        initList = [1]

        def dfs(target: int, init: List[int]) -> bool:
            if init[0] > target:
                return False
            elif init[0] == target:
                return True
            else:
                init[0] = 3 * init[0]
                print(init)
                return dfs(target, init)

        return dfs(n, initList)


if __name__ == '__main__':
    so = Solution()
    print(so.isPowerOfThree(27))
