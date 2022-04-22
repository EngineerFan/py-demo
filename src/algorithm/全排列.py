# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/7/3 10:14
# @Software    : PyCharm
# @Description : 全排列问题


from typing import List


class Solution:
    def recall(self, n: int, result: List[int], cur: int) -> None:
        if cur == n:
            if len(result) == n:
                print(result)
            return
        else:
            for i in range(1, n + 1):
                if i in result:
                      continue
                result.append(i)
                self.recall(n, result, cur + 1)


if __name__ == '__main__':
    so = Solution()
    n = 3
    so.recall(n, [], 1)
