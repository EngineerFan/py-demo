from typing import List
from typing import Set


class Solution:
    """
     1.graph 的长度范围为 [1, 100]
     2.graph[i] 中的元素的范围为 [0, graph.length - 1]。
     3.graph[i] 不会包含 i 或者有重复的值。
     4.图是无向的: 如果j 在 graph[i]里边, 那么 i 也会在 graph[j]里边。

     demo:
     示例 1:
     输入: [[1,3], [0,2], [1,3], [0,2]]
     输出: true
     解释:
       无向图如下:
             0----1
             |    |
             |    |
             3----2
       我们可以将节点分成两组: {0, 2} 和 {1, 3}。

    示例 2:
       输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
       输出: false
       解释:
      无向图如下:
             0----1
             | \  |
             |  \ |
             3----2
       我们不能将节点分割成两个独立的子集。

    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
          如果一条边的一个顶点在集合A = {} 中 ,则另一个顶点一定在集合 B = {} 中
        """
        node_list = list(range(0, len(graph)))
        for root, adjoin_list in enumerate(graph):
            la = list()
            lb = list()
            la.append(root)
            result = self.traverse(root, root, graph, la, lb, node_list)
            if result is None:
                continue
            else:
                return result
        return True

    """
    从第二个节点开始递归遍历 当前根节点的邻接节点集合
    """

    def traverse(self, current_node: int, iter_node: int, graph: List[List[int]], l1: List[int], l2: List[int],
                 node_list: List[int]) -> bool:
        # 每迭代一个节点，判断其邻接节点集合是否构成边，如果是，直接返回False，否则，True
        # 计算出当前迭代节点外的，邻接节点集合
        surplus_nodes = set(node_list) - (set(l1) | set(l2))
        for node in graph[iter_node]:
            coincide = set(graph[node]) & set(graph[iter_node])
            if len(coincide) > 0:
                # print('三角形集合:  ', iter_node, node, coincide)
                return False
            if node == current_node:
                if (len(l1) + len(l2)) == 3:
                    return False
                if len(surplus_nodes) == 0:
                    # 表示所有节点全部经过
                    if iter_node in l1:
                        l2.append(node)
                    if iter_node in l2:
                        l1.append(node)
                    print('l1: ', l1)
                    print('l2: ', l2)
                    if len((set(l1) & set(l2))) == 0:
                        continue
                    else:
                        return False
                else:
                    continue
            else:
                if node in surplus_nodes:
                    if iter_node in l1:
                        l2.append(node)
                    if iter_node in l2:
                        l1.append(node)
                    return self.traverse(current_node, node, graph, l1, l2, node_list)

                else:
                    continue


if __name__ == '__main__':
    solution = Solution()
    # True
    # array = [[1], [0, 3], [3], [1, 2]]
    # True
    # array = [[3], [2, 4], [1], [0, 4], [1, 3]]
    # True
    # array = [[1, 3], [0, 2], [1, 3], [0, 2]]
    # False
    # array = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
    #          [2, 4, 5, 6, 7, 8]]
    # True
    # array = [[], [3], [], [1], []]
    # False
    array = [[2, 3, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9],
             [1, 2, 3, 6, 9], [0, 1, 2, 3, 7, 8, 9], [0, 1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9],
             [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]
    print(solution.isBipartite(array))
