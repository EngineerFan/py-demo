# author  : Ryan
# datetime: 2020/8/19 15:23
# software: PyCharm

"""
description: 141. 环形链表

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


 

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        p = head.next
        headValList = [id(head)]
        while p is not None:
            if id(p) in headValList:
                return True
            else:
                headValList.append(id(p))
                p = p.next
        return False


if __name__ == '__main__':
    so = Solution()
    head = ListNode()
    print(so.hasCycle(head))
