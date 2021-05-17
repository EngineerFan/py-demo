# author  : Ryan
# datetime: 2021/3/9 10:10
# software: PyCharm

"""
description:

"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        s_list = list(S)
        flag = False
        op = -1
        while len(s_list) > 0:
            if len(s_list) == 1:
                return ''.join(s_list)
            for i in range(1, len(s_list)):
                if s_list[i] == s_list[i - 1]:
                    flag = True
                    op = i
                    break
            if flag:
                s_list.pop(op)
                s_list.pop(op - 1)
                op = -1
                flag = False
            else:
                break
        return ''.join(s_list)


print(Solution().removeDuplicates('abbaca'))
