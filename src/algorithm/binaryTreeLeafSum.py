# author  : Ryan
# datetime: 2020/8/25 15:53
# software: PyCharm

"""
description: 1302. 层数最深叶子节点的和

输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
 

提示：

树中节点数目在 1 到 10^4 之间。  二叉树层数 <= 15层
每个节点的值在 1 到 100 之间。


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        result = 1
        resultList = []
        resultValList = []

        def dfs(node: TreeNode, result: int, resultList: List[int]) -> None:
            if node is None:
                return

            if node.left is None and node.right is None:
                resultList.append(result)
                resultValList.append(node.val)
                return
            result += 1
            dfs(node.left, result, resultList)
            dfs(node.right, result, resultList)

        dfs(root, result, resultList)
        print(resultList)
        maxDeepVal = max(resultList)
        sumsList = [i for i, x in enumerate(resultList) if x == maxDeepVal]
        result = 0
        for val in sumsList:
            result = result + resultValList[val]
        return result


if __name__ == '__main__':
    so = Solution()
