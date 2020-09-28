# author  : Ryan
# datetime: 2020/9/28 13:01
# software: PyCharm

"""
description:  02.02. 返回倒数第 k 个节点

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

给定的 k 保证是有效的。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        prevNode, nextNode = head, head
        count = 1
        while count < k:
            nextNode = nextNode.next
            count += 1
        print('nextNode: ', nextNode.val)
        print('prevNode: ', prevNode.val)
        return
        while nextNode and nextNode.next:
            nextNode = nextNode.next
            prevNode = prevNode.next
        return prevNode.val
