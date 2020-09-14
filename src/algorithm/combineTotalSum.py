# author  : Ryan
# datetime: 2020/9/14 11:02
# software: PyCharm

"""
description: 组合综合

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。



说明：

所有数字都是正整数。

解集不能包含重复的组合。



示例 1:

输入: k = 3, n = 7

输出: [[1,2,4]]

示例 2:

输入: k = 3, n = 9

输出: [[1,2,6], [1,3,5], [2,3,4]]

"""
from typing import List


class Solution:

    def combinationSum(self, k: int, n: int) -> List[List[int]]:
        resultList = []

        def dfs(result: List[List[int]], re: List[int], start: int, total: int) -> None:
            if len(re) == k or total <= 0:
                if len(re) == k and total == 0:
                    l = re.copy()
                    result.append(l)
                return
            for i in range(start, 10):
                re.append(i)
                dfs(result, re, i + 1, total - i)
                re.remove(re[-1])

        dfs(resultList, [], 1, n)
        return resultList


if __name__ == '__main__':
    so = Solution()
    print(so.combinationSum(3, 9))
