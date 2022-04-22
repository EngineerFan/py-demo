# author  : Ryan
# datetime: 2022/3/23 10:21
# software: PyCharm

"""
description:

"""
from typing import List
import time


class TriedNode:
    def __init__(self):
        self.next = dict()


class TriedTree:
    def __init__(self):
        self.root = TriedNode()

    def buildTree(self, number: int) -> None:
        currentNode = self.root
        numberStr = str(number)
        for n in numberStr:
            if not n in currentNode.next:
                currentNode.next[n] = TriedNode()
            currentNode = currentNode.next[n]

    '''
        构建中获取第K小的字典序，并返回
    '''

    def buildTree2(self, number: int, k: int) -> None:
        currentNode = self.root
        numberStr = str(number)
        for n in numberStr:
            if not currentNode.next.get(n, None):
                currentNode.next[n] = TriedNode()
            currentNode = currentNode.next[n]

    def findKVal(self, k: int) -> int:
        currentNode = self.root
        seqList = []
        numberStr = ""

        def dfs(currentNode: TriedNode, seqList: List[str], k: int, numberStr: str):
            if not currentNode.next or k == len(seqList):
                return
            for key, nextNode in currentNode.next.items():
                numberStr += key
                seqList.append(numberStr)
                dfs(nextNode, seqList, k, numberStr)
                numberStr = numberStr[:-1]
                if k == len(seqList):
                    return

        dfs(currentNode, seqList, k, numberStr)
        return int(seqList[k - 1])


class Solution:

    def getSteps(self, curr: int, n: int) -> int:
        steps, first, last = 0, curr, curr
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last *= 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k:
            steps = self.getSteps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr


if __name__ == '__main__':
    so = Solution()
    print(so.findKthNumber(13, 2))
