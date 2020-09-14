# author  : Ryan
# datetime: 2020/9/14 18:27
# software: PyCharm

"""
description: 40. 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]

"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        resultList = []
        candidates.sort()
        # print(candidates)

        def dfs(result: List[List[int]], re: List[int], candidatesList: List[int], index: int, target: int,
                total: int) -> None:
            if total <= 0:
                if total == 0:
                    if re in result:
                        return
                    result.append(re.copy())
                return
            for i in range(index, len(candidatesList)):
                if candidatesList[i] > target or sum(re) + candidatesList[i] > target:
                    continue
                re.append(candidatesList[i])
                dfs(result, re, candidatesList, i + 1, target, total - candidatesList[i])
                del re[-1]

        dfs(resultList, [], candidates, 0, target, target)
        return resultList


if __name__ == '__main__':
    so = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(so.combinationSum2(candidates, target))
