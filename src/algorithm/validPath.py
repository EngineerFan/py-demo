import heapq
from typing import *


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p = list(i for i in range(n))
        print(p)

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def merge(a, b):
            p[find(a)] = find(b)

        for a, b in edges:
            merge(a, b)
        print(p)
        return find(source) == find(destination)


class Solution1:

    def test(self, nums: [int]):
        q = []
        for i in range(len(nums)):
            heapq.heappush(q, (-nums[i], i))
        print([nums[heapq.heappop(q)[1]] for _ in range(len(nums))])


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        result = [nums[q[0][1]]]
        for j in range(k, len(nums)):
            heapq.heappush(q, (-nums[j], j))
            while q[0][1] <= j - k:
                heapq.heappop(q)
            result.append(nums[q[0][1]])
        return result


class Solution3:
    def countAsterisks(self, s: str) -> int:
        p1, p2, p3, star_count = -1, -1, 0, 0
        strList = list(s)
        for i in range(len(strList)):
            if strList[i] == '|' and p1 == -1:
                p1 = i
                star_count += strList[p3:i].count('*')
            if strList[i] == '|' and p1 != i and p2 == -1:
                p2 = i
                p3 = p2 + 1
            if p1 != p2 != -1:
                p1 = -1
                p2 = -1
        star_count += strList[p3:].count('*')
        return star_count


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution4:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head, tempNode, prevNode = list1, list1.next, list1
        i = 1
        tailNode = list2
        while tailNode:
            tailNode = tailNode.next
        while tempNode:
            if i == a:
                prevNode.next = list2
            if i == b:
                tailNode.next = tempNode.next
                tempNode.next = None
                break
            prevNode = tempNode
            tempNode = tempNode.next
            i += 1
        return head


from collections import *


class Solution5:
    def decodeMessage(self, key: str, message: str) -> str:
        od = OrderedDict()
        i = 97
        for k in key:
            if k == ' ':
                continue
            if od.get(k, None):
                continue
            alph = chr(i)
            od[k] = alph
            i = i + 1
        result = ''
        for m in message:
            if od.get(m, None):
                result += od[m]
            if m == ' ':
                result += m
        return result


if __name__ == '__main__':
    # so = Solution()
    # print(so.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
    # so1 = Solution1()
    # print(so1.test(nums=[1, 3, 2, 4, 5, 6, 7, 10, 9]))
    # so2 = Solution2()
    # print(so2.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    # so3 = Solution3()
    # print(so3.countAsterisks(s="*||||**||*||**|**||*|||**"))
    # so4 = Solution4()
    # print(so4.mergeInBetween(list1=[], a=1, b=4, list2=[]))

    so5 = Solution5()
    print(so5.decodeMessage(key='eljuxhpwnyrdgtqkviszcfmabo', message='zwx hnfx lqantp mnoeius ycgk vcnjrdb'))
