# author  : Ryan
# datetime: 2020/8/4 16:25
# software: PyCharm

"""
description:


给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        l_0 = l1.val + l2.val
        if int(l_0 / 10) != 0:
            count = int(l_0 / 10)
        l = ListNode((l_0 % 10))
        nextNode = l

        while True:
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is None and l2 is None:
                if count != 0:
                    node = ListNode(count)
                    nextNode.next = node
                    nextNode = nextNode.next
                break
            elif l1 is None and l2 is not None:
                if count != 0:
                    tmp_count = count + l2.val
                    real_val = tmp_count % 10
                    count = int(tmp_count / 10)
                else:
                    count = int(l2.val / 10)
                    real_val = l2.val % 10
                node = ListNode(real_val)
                nextNode.next = node
                nextNode = nextNode.next

            elif l1 is not None and l2 is None:
                if count != 0:
                    tmp_count = count + l1.val
                    real_val = tmp_count % 10
                    count = int(tmp_count / 10)
                else:
                    count = int(l1.val / 10)
                    real_val = l1.val % 10
                node = ListNode(real_val)
                nextNode.next = node
                nextNode = nextNode.next
            else:
                if count != 0:
                    tmp_count = count + l1.val + l2.val
                    real_val = tmp_count % 10
                    count = int(tmp_count / 10)
                else:
                    count = int((l1.val + l2.val) / 10)
                    real_val = (l1.val + l2.val) % 10
                node = ListNode(real_val)
                nextNode.next = node
                nextNode = nextNode.next
        return l


if __name__ == '__main__':
    so = Solution()
    l_2 = ListNode(1)
    l_4 = ListNode(8)
    # l_3 = ListNode(3)
    l_2.next = l_4
    # l_4.next = l_3

    l_5 = ListNode(0)
    # l_6 = ListNode(6)
    # l_2_4 = ListNode(4)
    # l_5.next = l_6
    # l_6.next = l_2_4
    list_node = so.addTwoNumbers(l_2, l_5)
    print(list_node)
