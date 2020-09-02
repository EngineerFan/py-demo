# author  : Ryan
# datetime: 2020/9/2 11:09
# software: PyCharm

"""
description: 21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergeList = ListNode()
        newHeadNode = mergeList
        while True:
            if l1 is None and l2 is None:
                break
            if l1 is None and l2 is not None:
                newNode = ListNode(l2.val)
                mergeList.next = newNode
                mergeList = newNode
                l2 = l2.next
                continue
            if l1 is not None and l2 is None:
                newNode = ListNode(l1.val)
                mergeList.next = newNode
                mergeList = newNode
                l1 = l1.next
                continue
            if l1.val <= l2.val:
                newNode = ListNode(l1.val)
                mergeList.next = newNode
                mergeList = newNode
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                mergeList.next = newNode
                mergeList = newNode
                l2 = l2.next

        return newHeadNode.next
