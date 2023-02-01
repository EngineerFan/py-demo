'''
给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。

每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。

请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。



'''

from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, self.bfs(grid, i, j))
        return result

    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        m, n = len(grid), len(grid[0])
        if i >= m or j >= n or i < 0 or j < 0:
            return 0
        if grid[i][j] == 0:
            return grid[i][j]
        grid[i][j] = 0
        return self.bfs(grid, i, j - 1) + self.bfs(grid, i, j + 1) + self.bfs(grid, i - 1, j) + self.bfs(grid, i + 1,
                                                                                                         j) + 1


class SolutionCombination:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, 0, [], target, result)
        print(result)
        return result

    def backtracking(self, condidates: List[int], index: int, tmp: List[int], target: int, result: List[List[int]]):
        if sum(tmp) > target:
            return
        if sum(tmp) == target:
            result.append(tmp[:])
            return
        for j in range(index, len(condidates)):
            tmp.append(condidates[j])
            self.backtracking(condidates, j, tmp, target, result)
            tmp.pop()


if __name__ == '__main__':
    # so = Solution()
    # print(so.minOperations(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2]))
    so = SolutionCombination()
    so.combinationSum(candidates=[2, 3, 6, 7], target=7)
