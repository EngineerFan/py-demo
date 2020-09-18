# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/18 22:10
# @Software    : PyCharm
# @Description : 剑指 Offer 06. 从尾到头打印链表


"""

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]


限制：

0 <= 链表长度 <= 10000

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        resultList = []
        while head:
            resultList.append(head.val)
            head = head.next
        resultList.reverse()
        return resultList
