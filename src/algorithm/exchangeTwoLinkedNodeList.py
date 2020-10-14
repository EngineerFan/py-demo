# author  : Ryan
# datetime: 2020/10/13 19:07
# software: PyCharm

"""
description: 24. 两两交换链表中的节点


给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        aPointNode, bPointNode, cPointNode = None, head, head
        while cPointNode.next:
            cPointNode = cPointNode.next
            if not cPointNode:
                break
            # 执行交换操作
            if bPointNode == head:
                bPointNode.next = cPointNode.next
                cPointNode.next = bPointNode
            else:
                bPointNode.next = cPointNode.next
                cPointNode.next = bPointNode
                aPointNode.next = cPointNode

            # 交换后节点赋值给A节点，令A节点作为下一组交换的头节点
            aPointNode = bPointNode
            bPointNode, cPointNode = bPointNode.next, bPointNode.next
            if not bPointNode:
                break
        return head
