# author  : Ryan
# datetime: 2020/10/22 12:54
# software: PyCharm

"""
description:

"""

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dictMap = {}
        for i, e in enumerate(list(S)):
            dictMap[e] = i

        result = []
        current = dictMap[S[0]]
        for i, e in enumerate(list(S)):
            if dictMap[e] > current:
                current = dictMap[e]
            if current == i:
                result.append(i + 1 - sum(result))
        return result


if __name__ == '__main__':
    so = Solution()
    S = 'ababcbacadefegdehijhklij'
    print(so.partitionLabels(S))
