# author  : Ryan
# datetime: 2020/8/20 19:31
# software: PyCharm

"""
description: 231. 2的幂

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            remainder = n % 2
            if remainder == 0:
                n = n / 2
                continue
            if n == 1:
                return True
            return False


if __name__ == '__main__':
    so = Solution()
    n = 15
    print(so.isPowerOfTwo(n))
