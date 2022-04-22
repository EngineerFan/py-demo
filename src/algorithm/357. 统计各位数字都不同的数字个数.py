# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/4/11 11:18
# @Software    : PyCharm
# @Description : 357. 统计各位数字都不同的数字个数


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        result, current = 10, 9
        for i in range(n - 1):
            current *= 9 - i
            result += current
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.countNumbersWithUniqueDigits(2))
