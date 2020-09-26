# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/25 21:44
# @Software    : PyCharm
# @Description : 590. N叉树的后序遍历

"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :







返回其后序遍历: [5,6,3,2,4,1].

"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        resultList = []
        if root is None:
            return resultList

        q = [root]
        dequeueNodeList = []
        while len(q) != 0:
            tempNode = q[0]
            childrenLength = len(tempNode.children)
            # print(childrenLength)
            # print('resultList: ',resultList)
            if childrenLength == 0:
                node = q.pop(0)
                resultList.append(node.val)
                dequeueNodeList.append(node)
                if len(q) == 0:
                    break
                tempNode = q[0]
                childrenLength = len(tempNode.children)
            if tempNode in dequeueNodeList:
                continue
            elif set(tempNode.children).issubset(dequeueNodeList):
                # print(1)
                resultList.append(tempNode.val)
                dequeueNodeList.append(q.pop(0))
                continue
            if childrenLength != 0:
                for i in range(childrenLength):
                    q.insert(i, tempNode.children[i])
        return resultList
