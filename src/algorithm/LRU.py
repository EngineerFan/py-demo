import random
import typing


class DNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DLinkedList:

    def __init__(self, size: int = 0, head: DNode = DNode(0, 0), tail: DNode = DNode(0, 0)):
        self.size = size
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def addLast(self, node: DNode):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node: DNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        firstDNode = self.head.next
        self.remove(firstDNode)
        return firstDNode

    def size(self):
        return self.size()


class LruCache:

    def __init__(self, cap: int):
        self.dictMap = dict()
        self.dList = DLinkedList()
        self.cap = cap

    def __markRecently(self, key: str):
        node = self.dictMap.get(key, None)
        if node:
            self.dList.remove(node)
            self.dList.addLast(node)

    def addRecently(self, key, val):
        node = DNode(key, val)
        self.dList.addLast(node)
        self.dictMap[key] = node

    def removeKey(self, key):
        node = self.dictMap.get(key)
        del self.dictMap[key]
        self.dList.remove(node)

    def removeNoUseKey(self):
        node = self.dList.removeFirst()
        del self.dictMap[node.key]

    def get(self, key):
        if not self.dictMap.get(key, None):
            return None
        self.__markRecently(key)
        return self.dictMap[key].val

    def put(self, key, val):
        if self.dictMap.get(key, None):
            self.removeKey(key)
            self.addRecently(key, val)
            return
        if self.cap == getattr(self.dList, 'size'):
            self.removeNoUseKey()
        self.addRecently(key, val)


if __name__ == '__main__':
    cache = LruCache(100)
    for i in range(20):
        cache.put(i, random.randint(100, 200))
    print(cache)
    print(cache.get(5))
    print('finish')

