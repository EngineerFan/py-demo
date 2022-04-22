# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/3/19 21:00
# @Software    : PyCharm
# @Description :
from typing import List


class TriedNode:
    def __init__(self):
        self.isFinish = False
        self.next = dict()


class TriedTree:

    def __init__(self):
        self.root = TriedNode()
        self.dictElementList = list()

    def insert(self, number: int) -> None:
        currentNode = self.root
        numberStr = str(number)
        for i in range(len(numberStr)):
            if currentNode.next.get(numberStr[i], None) is None:
                currentNode.next[numberStr[i]] = TriedNode()
                currentNode.isFinish = False
                currentNode.next[numberStr[i]].isFinish = True
            currentNode = currentNode.next.get(numberStr[i])

    def dictSeqOrder(self) -> List[int]:
        resultList = self.dictElementList
        currentNode = self.root
        def dfs(currentNode: TriedNode, resultList: List[int], temp: str) -> None:
            if not currentNode.next:
                return
            for d in currentNode.next.items():
                temp += d[0]
                resultList.append(int(temp))
                dfs(d[1], resultList, temp)
                temp = temp[:-1]

        dfs(currentNode, resultList, "")
        return resultList


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        triedTree = TriedTree()
        for i in range(1, n + 1):
            triedTree.insert(i)
        triedTree.dictSeqOrder()

if __name__ == '__main__':
    so = Solution()
    print(so.lexicalOrder(12))
