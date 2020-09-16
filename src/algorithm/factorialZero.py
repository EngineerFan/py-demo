# author  : Ryan
# datetime: 2020/8/21 13:13
# software: PyCharm

"""
description: 阶乘尾数


设计一个算法，算出 n 阶乘有多少个尾随零。

示例 1:

输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
示例 2:

输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
说明: 你算法的时间复杂度应为 O(log n) 。


"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n: int) -> int:
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        result = factorial(n)
        count = 0

        return count


if __name__ == '__main__':
    so = Solution()
    n = 1808548329
    print(so.trailingZeroes(n))
