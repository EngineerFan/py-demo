# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/7/24 15:34
# @Software    : PyCharm
# @Description : 除数博弈
import random


class Solution:

    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        if N == 2:
            return True
        count = 1
        while True:
            rand_number = random.randint(1, N - 1)

            if (N % rand_number) == 0:
                N = N - rand_number
                if N == 0 or N == 1:
                    return False if (count % 2) == 0 else True
                else:
                    count = count + 1
            else:
                rand_number = random.randint(1, N - 1)


if __name__ == '__main__':
    solution = Solution()
    N = 4
    print(solution.divisorGame(N))
