from collections import *


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digitMap = Counter()
        d = ''
        for i in range(len(word)):
            if word[i].isdigit():
                d += word[i]
                if i == len(word) - 1:
                    digitMap[int(d)] = 1
            else:
                if d != '':
                    digitMap[int(d)] = 1
                    d = ''
        # print(digitMap)
        return len(digitMap)


if __name__ == '__main__':
    so = Solution()
    print(so.numDifferentIntegers(word='a123bc34d8ef34'))
