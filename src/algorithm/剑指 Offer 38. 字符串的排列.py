# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/22 19:55
# @Software    : PyCharm
# @Description :
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        c, result = list(s), []

        def dfs(x):
            if x == len(c) - 1:
                result.append("".join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x + 1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return result


so = Solution()
so.permutation("abc")
