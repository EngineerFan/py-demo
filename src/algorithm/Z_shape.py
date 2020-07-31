# author  : Ryan
# datetime: 2020/7/29 13:13
# software: PyCharm

"""
description: Z 型

"""
from queue import Queue


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_list = list(s)
        s_list.reverse()
        s_length = len(s_list)
        print(s_length)
        if s_length <= numRows or numRows == 1:
            return s
        if numRows == 2:
            l = list()
            r = list()
            for i in range(s_length):
                if i == 0:
                    l.append(s_list.pop())
                    continue
                if i % 2 == 0:
                    l.append(s_list.pop())
                else:
                    r.append(s_list.pop())
            print('l: ', l)
            print('r: ', r)
            return ''.join(l) + ''.join(r)
        col_nums = 0
        # 两列一组 共有组数
        groups = int(s_length / ((numRows - 1) * 2))
        surplus = s_length % ((numRows - 1) * 2)
        if groups == 0:
            if surplus <= numRows:
                col_nums = 1
            else:
                col_nums = 1 + (surplus - numRows)
        else:
            if surplus == 0:
                col_nums = groups + groups * (numRows - 2)
            elif surplus <= numRows:
                col_nums = groups + groups * (numRows - 2) + 1
            else:
                col_nums = groups + groups * (numRows - 2) + 1 + (surplus - numRows)

        print('(', numRows, ',', col_nums, ')')
        matrix = [[0 for i in range(col_nums)] for j in range(numRows)]
        row_add_counter = 0
        is_traverse_flag = True
        for c in range(col_nums):
            if row_add_counter == numRows - 1:
                is_traverse_flag = False

            # 解决对角遍历问题
            if is_traverse_flag:
                for r in range(numRows):
                    row_add_counter = r
                    if len(s_list) != 0:
                        matrix[r][c] = s_list.pop()
            else:
                row_add_counter = row_add_counter - 1
                if row_add_counter == 1:
                    is_traverse_flag = True
                    matrix[row_add_counter][c] = s_list.pop()
                else:
                    matrix[row_add_counter][c] = s_list.pop()

        print(matrix)
        result_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    result_list.append(matrix[i][j])
        return ''.join(result_list)


if __name__ == '__main__':
    so = Solution()
    s = 'PAYPALISHIRING'
    numRows = 9
    result = so.convert(s, numRows)
    print(result)
