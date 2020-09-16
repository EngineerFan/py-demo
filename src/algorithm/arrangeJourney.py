# author  : Ryan
# datetime: 2020/8/27 8:51
# software: PyCharm

"""
description: 332. 重新安排行程

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。


"""
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pathList = []
        length = len(tickets)

        def dfs(destination: str, tickets_bk: List[List[int]], length_bk: int, path: List[int],
                pathList: List[List[int]]) -> None:
            path.append(destination)
            for i in range(length_bk):
                if destination == tickets_bk[i][0]:
                    dest = tickets_bk[i][1]
                    tickets_bk.remove(tickets_bk[i])
                    dfs(dest, tickets_bk, len(tickets_bk), path, pathList)
                    break

        for i in range(length):
            if tickets[i][0] == 'JFK':
                path = []
                path.append(tickets[i][0])
                tickets_bk = tickets.copy()
                tickets_bk.remove(tickets[i])
                dfs(tickets[i][1], tickets_bk, len(tickets_bk), path, pathList)
                pathListLength = len(pathList)
                if pathListLength > 0:
                    pathLength = len(path)
                    for j in range(pathLength):
                        try:
                            if path[j] == pathList[0][j]:
                                continue
                            else:
                                for k in range(3):
                                    if path[j][k] == pathList[0][j][k]:
                                        continue
                                    elif path[j][k] > pathList[0][j][k]:
                                        break
                                    else:
                                        pathList.remove(pathList[0])
                                        pathList.append(path)
                                        break
                                break
                        except IndexError:
                            pass
                else:
                    pathList.append(path)
        return pathList[0]


if __name__ == '__main__':
    so = Solution()
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(so.findItinerary(tickets=tickets))
