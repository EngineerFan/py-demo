# author  : Ryan
# datetime: 2020/9/25 14:31
# software: PyCharm

"""
description: 589. N叉树的前序遍历


给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 



 

返回其前序遍历: [1,3,5,6,2,4]。

 

说明: 递归法很简单，你可以使用迭代法完成此题吗?


"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        q = [root]
        resultList = []
        while len(q) != 0:
            tempNode = q[0]
            q.pop(0)
            resultList.append(tempNode.val)
            if tempNode.children is None or len(tempNode.children) == 0:
                continue
            else:
                if len(q) == 0:
                    q.extend(tempNode.children)
                else:
                    for i in range(len(tempNode.children)):
                        q.insert(i, tempNode.children[i])
        return resultList
