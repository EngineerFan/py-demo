# author  : Ryan
# datetime: 2020/7/28 15:30
# software: PyCharm

"""
description: 堆箱子

"""
from typing import List


class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        if len(box) >= 3000:
            return 0


if __name__ == '__main__':
    so = Solution()
    print(so.pileBox(None))
