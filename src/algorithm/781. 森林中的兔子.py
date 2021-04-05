# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/4/4 18:10
# @Software    : PyCharm
# @Description : 781. 森林中的兔子

from typing import List
import collections


class Solution:
    ## [1,0,1,0,0]
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        aswer = collections.Counter(answers)
        count = 0
        for k, v in aswer.items():
            if k == 0:
                count = count + v
            else:
                if v == 1:
                    count = count + k + 1
                else:
                    # 可能存在不同颜色的兔子
                    if v <= k + 1:
                        count = count + k + 1
                    else:
                        t = v // (k + 1)
                        s = v % (k + 1)
                        if s != 0:
                            count = count + (t + 1) * (k + 1)
                        else:
                            count = count + t * (k + 1)
        return count


so = Solution()
print(so.numRabbits([0, 1, 0, 2, 0, 1, 0, 2, 1, 1]))
