from typing import *


def backTrace(nums: List[int], usedList: List[bool], trackList: List[int], result: List[List[int]], repeatDict: Dict) -> \
        List[List[int]]:
    if len(trackList) == len(nums):
        tmp = trackList[:]
        tmp1 = [str(i) for i in tmp]
        if not repeatDict.get(''.join(tmp1), None):
            repeatDict[''.join(tmp1)] = 1
            result.append(tmp)
        return result
    for k, v in enumerate(nums):
        if usedList[k]:
            continue
        trackList.append(v)
        usedList[k] = True
        backTrace(nums, usedList, trackList, result, repeatDict)
        trackList.pop(-1)
        usedList[k] = False


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        usedList = [False] * len(nums)
        repeatDict = dict()
        backTrace(nums, usedList, [], result, repeatDict)
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.permute(nums=[1, 2, 3, 3]))
