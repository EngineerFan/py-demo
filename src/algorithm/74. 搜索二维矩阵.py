from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        for i in range(rows):
            if i + 1 < rows and target >= matrix[i][0] and target < matrix[i + 1][0]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
            elif rows == 1:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
            elif i == rows - 1 and target >= matrix[i][0]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
        return False


so = Solution()
print(so.searchMatrix([[1], [3]], 3))
