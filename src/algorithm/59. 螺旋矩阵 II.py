from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        x, y = 0, 0
        i = 1
        matrix[x][y] = i
        while True:
            if y + 1 < n and matrix[x][y + 1] == 0:
                i = i + 1
                matrix[x][y + 1] = i
                y += 1
            elif x + 1 < n and matrix[x + 1][y] == 0:
                i = i + 1
                matrix[x + 1][y] = i
                x += 1
            elif y - 1 > -1 and matrix[x][y - 1] == 0:
                i = i + 1
                matrix[x][y - 1] = i
                y -= 1
            elif x - 1 > -1 and matrix[x - 1][y] == 0:
                i = i + 1
                matrix[x - 1][y] = i
                x -= 1
            else:
                break
        return matrix

so = Solution()
print(so.generateMatrix(3))