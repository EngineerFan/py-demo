# author  : Ryan
# datetime: 2020/10/14 16:30
# software: PyCharm

"""
description: 1002. 查找常用字符


给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]


提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母

"""
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        A0 = list(set(A[0]))
        for i in range(len(A0)):
            flagNumber, otherArrIsContain = True, True
            count = A[0].count(A0[i])
            minCount = count
            for j in range(1, len(A)):
                try:
                    A[j].index(A0[i])
                    tempCount = A[j].count(A0[i])
                    if count > tempCount:
                        minCount = min(minCount, tempCount)
                    elif count <= tempCount:
                        minCount = min(minCount, count)
                except ValueError:
                    otherArrIsContain = False
            if otherArrIsContain and flagNumber:
                for k in range(minCount):
                    result.append(A0[i])
            elif otherArrIsContain and not flagNumber:
                result.append(A0[i])
            else:
                pass

        return result


if __name__ == '__main__':
    so = Solution()
    A = ["bcaddcdd", "cbcdccdd", "ddccbdda", "dacbbdad", "dababdcb", "bccbdaad", "dbccbabd", "accdddda"]
    print(so.commonChars(A))
