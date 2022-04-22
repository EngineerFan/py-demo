# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/2/28 22:23
# @Software    : PyCharm
# @Description :

from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        delta = [0] * n
        ans, cnt, zero = 0, 0, n

        def dfs(pos: int) -> None:
            nonlocal ans, cnt, zero
            if pos == len(requests):
                if zero == n:
                    ans = max(ans, cnt)
                return
            dfs(pos + 1)
            z = zero
            cnt += 1
            x, y = requests[pos]
            zero -= delta[x] == 0
            delta[x] -= 1
            zero += delta[x] == 0
            zero -= delta[y] == 0
            delta[y] += 1
            zero += delta[y] == 0
            dfs(pos + 1)
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1
            zero = z

        dfs(0)
        return ans


if __name__ == '__main__':

    print((1 == 1) + 1)
    print((0 == 1) - 1)
    so = Solution()
    print(so.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
