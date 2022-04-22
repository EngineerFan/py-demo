# author  : Ryan
# datetime: 2022/3/24 9:20
# software: PyCharm

"""
description:图片平滑器

"""

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        result = [[0] * col for _ in range(row)]
        print('img: ', img)
        for i in range(row):
            for j in range(col):
                count = 1
                if i - 1 >= 0:
                    result[i][j] += img[i - 1][j]
                    count += 1
                if i + 1 < row:
                    result[i][j] += img[i + 1][j]
                    count += 1
                if j - 1 >= 0:
                    result[i][j] += img[i][j - 1]
                    count += 1
                if j + 1 < col:
                    result[i][j] += img[i][j + 1]
                    count += 1
                if i + 1 < row and j + 1 < col:
                    result[i][j] += img[i + 1][j + 1]
                    count += 1
                if i + 1 < row and j - 1 >= 0:
                    result[i][j] += img[i + 1][j - 1]
                    count += 1
                if i - 1 >= row and j - 1 >= 0:
                    result[i][j] += img[i - 1][j - 1]
                    count += 1
                if i - 1 >= row and j + 1 < col:
                    result[i][j] += img[i - 1][j + 1]
                    count += 1

                result[i][j] = (img[i][j] + result[i][j]) // count
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
