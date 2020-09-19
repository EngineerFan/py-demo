# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/19 11:54
# @Software    : PyCharm
# @Description : 剑指 Offer 25. 合并两个排序的链表

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultNode = ListNode()
        temp = resultNode
        while True:
            if l1 and l2:
                if l1.val > l2.val:
                    temp.next = ListNode(l2.val)
                    temp = temp.next
                    l2 = l2.next
                    continue
                elif l1.val < l2.val:
                    temp.next = ListNode(l1.val)
                    temp = temp.next
                    l1 = l1.next
                    continue
                elif l1.val == l2.val:
                    temp.next = ListNode(l1.val)
                    temp = temp.next
                    temp.next = ListNode(l2.val)
                    temp = temp.next
                    l1 = l1.next
                    l2 = l2.next
                    continue

            elif l1 is not None and l2 is None:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            elif l1 is None and l2 is not None:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            elif l1 is None and l2 is None:
                break

        return resultNode.next
