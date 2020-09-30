# author  : Ryan
# datetime: 2020/9/28 14:02
# software: PyCharm

"""
description: 445. 两数相加 II

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7


"""

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insertList(self, nodeValList: List[int]):
        length = len(nodeValList)
        if len(nodeValList) == 0:
            return ListNode(None)
        headNode, tempNode = None, None
        for i in range(length):
            if i == 0:
                headNode = ListNode(nodeValList[i])
                tempNode = headNode
            else:
                node = ListNode(nodeValList[i])
                tempNode.next = node
                tempNode = node
        return headNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        while l1 or l2:
            if l1:
                list1.insert(0, l1.val)
                l1 = l1.next
            if l2:
                list2.insert(0, l2.val)
                l2 = l2.next

        print('list1: ', list1)
        print('list2: ', list2)
        length1, length2 = len(list1), len(list2)
        resultValList = []
        resultHeadNode, tempNode = None, None
        addCount = 0
        if length1 == length2:
            for i in range(length2):
                if list1[i] + list2[i] + addCount >= 10:
                    resultValList.insert(0, list1[i] + list2[i] + addCount - 10)
                    addCount = 1
                else:
                    resultValList.insert(0, list1[i] + list2[i] + addCount)
                    addCount = 0
            if addCount == 1:
                resultValList.insert(0, 1)

        elif length1 > length2:
            for i in range(length1):
                if i <= length2 - 1 and list1[i] + list2[i] + addCount >= 10:
                    resultValList.insert(0, list1[i] + list2[i] + addCount - 10)
                    addCount = 1
                elif i <= length2 - 1 and list1[i] + list2[i] + addCount < 10:
                    resultValList.insert(0, list1[i] + list2[i] + addCount)
                    addCount = 0
                elif i >= length2:
                    if list1[i] + addCount >= 10:
                        resultValList.insert(0, list1[i] + addCount - 10)
                        addCount = 1
                    else:
                        resultValList.insert(0, list1[i] + addCount)
                        addCount = 0
                else:
                    continue
            if addCount == 1:
                resultValList.insert(0, 1)
        else:
            for i in range(length2):
                if i <= length1 - 1 and list1[i] + list2[i] + addCount >= 10:
                    resultValList.insert(0, list1[i] + list2[i] + addCount - 10)
                    addCount = 1
                elif i <= length1 - 1 and list1[i] + list2[i] + addCount < 10:
                    resultValList.insert(0, list1[i] + list2[i] + addCount)
                    addCount = 0
                elif i >= length1:
                    if list2[i] + addCount >= 10:
                        resultValList.insert(0, list2[i] + addCount - 10)
                        addCount = 1
                    else:
                        resultValList.insert(0, list2[i] + addCount)
                        addCount = 0
                else:
                    continue
            if addCount == 1:
                resultValList.insert(0, 1)

        for i in range(len(resultValList)):
            if i == 0:
                resultHeadNode = ListNode(resultValList[i])
                tempNode = resultHeadNode
            else:
                node = ListNode(resultValList[i])
                tempNode.next = node
                tempNode = node
        return resultHeadNode
