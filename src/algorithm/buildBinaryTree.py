# author  : Ryan
# datetime: 2021/11/24 9:12
# software: PyCharm

"""
description:

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, items):
        root = self.buildTree(None, items)
        self.root = root

    ## 完全版
    # def buildTree(self, root, items, i) -> TreeNode:
    #     if i < len(items):
    #         if items[i] is None:
    #             return None
    #         else:
    #             root = TreeNode(items[i])
    #             root.left = self.buildTree(root.left, items, 2 * i + 1)
    #             root.right = self.buildTree(root.right, items, 2 * i + 2)
    #             return root
    #     return root

    def buildTree(self, root, items) -> TreeNode:
        if not items:
            return None
        root = TreeNode(items[0])
        items.pop(0)
        q = [root]
        while q and items:
            temp = q[0]
            q.remove(q[0])
            if temp:
                left = items[0]
                temp.left = TreeNode(left) if left else None
                items.remove(items[0])
                q.append(temp.left)
                try:
                    right = items[0]
                    temp.right = TreeNode(right) if right else None
                    items.remove(items[0])
                    q.append(temp.right)
                except:
                    pass
        return root

    def maxDepth(self, root: TreeNode) -> int:
        result = [1, 0]
        if root is None:
            return result[1]
        self.dfs(root, result)
        return result[1]

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)

        right = self.minDepth(root.right)
        return (left + right + 1) if (left == 0 or right == 0) else min(left, right) + 1

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass


if __name__ == '__main__':
    items = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    tree = Tree(items)
    print(tree.hasPathSum(root=tree.root, targetSum=targetSum))
