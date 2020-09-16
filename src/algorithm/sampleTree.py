# author  : Ryan
# datetime: 2020/8/19 10:54
# software: PyCharm

"""
description:  100. 相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pList = []
        qList = []

        def traverse(rootNode: TreeNode, nodeList: List) -> TreeNode:
            nodeList.append(rootNode.val)
            if rootNode.left is None:
                nodeList.append(None)
            else:
                pass
            if rootNode.right is None:
                nodeList.append(None)
            else:
                pass
            pass

        pass


if __name__ == '__main__':
    s = Solution()
    p = TreeNode()
    q = TreeNode()
    print(s.isSameTree(p, q))
