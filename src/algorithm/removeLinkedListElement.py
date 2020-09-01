# author  : Ryan
# datetime: 2020/9/1 10:37
# software: PyCharm

"""
description: 203. 移除链表元素

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        tmpNode, preTmpNode = head, ListNode(None)
        preTmpNode.next = head
        tempHeadNode = preTmpNode
        while tmpNode:
            if tmpNode.val == val:
                preTmpNode.next = tmpNode.next
                tmpNode = preTmpNode.next
                continue
            tmpNode = tmpNode.next
            preTmpNode = preTmpNode.next
        return tempHeadNode


if __name__ == '__main__':
    node1 = ListNode(None)
    print(node1)
    node2 = node1
    print(node2)
    node2.val = 23
    print(node1.val)
