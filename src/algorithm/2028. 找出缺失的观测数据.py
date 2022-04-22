# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/27 09:44
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rollsLength, rollsSum = len(rolls), sum(rolls)
        totalSum = mean * (rollsLength + n)
        restSum = totalSum - rollsSum
        yu, sh = restSum % n, restSum // n
        if restSum / n > 6 or restSum <= 0 or sh == 0:
            return []
        result = [sh] * n
        if sh + yu <= 6:
            result[0] += yu
        elif yu <= n:
            for i in range(yu):
                result[i] += 1
        else:
            return []
        return result


if __name__ == '__main__':
    so = Solution()

    print(so.missingRolls(
        [4, 2, 2, 5, 4, 5, 4, 5, 3, 3, 6, 1, 2, 4, 2, 1, 6, 5, 4, 2, 3, 4, 2, 3, 3, 5, 4, 1, 4, 4, 5, 3, 6, 1, 5, 2, 3,
         3, 6, 1, 6, 4, 1, 3],
        2,
        53,
    ))
