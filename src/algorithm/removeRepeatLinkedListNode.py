# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/13 08:40
# @Software    : PyCharm
# @Description : 面试题 02.01. 移除重复节点


'''

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        tmpList = []
        headPoint = head
        countPoint = ListNode(None)
        countPoint.next = head
        while head:
            if len(tmpList) != 0:
                try:
                    tmpList.index(head.val)
                    countPoint.next = head.next
                    head = head.next
                    continue
                except ValueError:
                    tmpList.append(head.val)
            else:
                tmpList.append(head.val)
            head = head.next
            countPoint = countPoint.next
        return headPoint
