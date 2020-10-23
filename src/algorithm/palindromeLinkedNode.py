# author  : Ryan
# datetime: 2020/10/23 8:44
# software: PyCharm

"""
description: 234. 回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next
        length = len(nodeList)
        if length == 0 or length == 1 or (length == 2 and nodeList[0] == nodeList[1]):
            return True
        if length % 2 == 0:
            mid1 = int(length / 2) - 1
            mid2 = int(length / 2)
            i, j = mid1, mid2
            while i > -1 and j < length:
                if nodeList[i] != nodeList[j]:
                    return False
                i = i - 1
                j = j + 1
        else:
            mid = int(length / 2)
            i = mid - 1
            while i > -1:
                if nodeList[i] != nodeList[mid + mid - i]:
                    return False
                i = i - 1
        return True



















