# author  : Ryan
# datetime: 2020/9/22 17:13
# software: PyCharm

"""
description: 551. 学生出勤记录 I

给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False


"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        aCount = 0
        sList = list(s)
        length = len(sList)
        for i in range(length):
            if sList[i] == 'P':
                continue
            elif sList[i] == 'A':
                aCount += 1
                if aCount > 1:
                    return False
            else:
                if i - 1 > -1 and i + 1 < length and sList[i - 1] == sList[i] == sList[i + 1]:
                    return False
        return True
