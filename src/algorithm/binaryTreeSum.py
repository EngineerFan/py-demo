# author  : Ryan
# datetime: 2020/8/25 14:14
# software: PyCharm

"""
description: 二叉树中和为某一值的路径


输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000


"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        def dfs(node: TreeNode, sum: int, subList: List[int], result: List[List[int]]) -> None:
            if node is None:
                return
            tmpList = []
            tmpList = tmpList + subList
            tmpList.append(node.val)
            if node.left is None and node.right is None:
                if node.val == sum:
                    result.append(tmpList)
                    return
            dfs(node.left, sum - node.val, tmpList, result)
            dfs(node.right, sum - node.val, tmpList, result)

        dfs(root, sum, list(), result)
        return result


if __name__ == '__main__':
    so = Solution()
