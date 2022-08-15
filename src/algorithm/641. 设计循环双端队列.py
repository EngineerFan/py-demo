# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2022/8/15 21:53
# @Software    : PyCharm
# @Description :


class MyCircularDeque:

    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.queue = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.isEmpty():
                self.front = self.rear = 0
                self.queue.insert(self.front, value)
                return True
            else:
                if self.front - 1 >= 0:
                    self.queue.insert(self.front - 1, value)
                    self.front = self.front - 1
                    return True
                else:
                    self.queue.insert(self.size - 1, value)
                    self.front = self.size - 1
                    return True

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue.append(value)
            return True
        else:
            if self.rear + 1 <= self.size - 1:
                self.queue.append(value)
                self.rear = self.rear + 1
                return True
            else:
                self.queue.append(value)
                self.rear = 0
                return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        del self.queue[self.front]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        del self.queue[self.rear]
        return True

    def getFront(self) -> int:
        return self.queue[self.front]

    def getRear(self) -> int:
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        return True

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyCircularDeque(5)
    param_1 = obj.insertFront(7)
    param_2 = obj.insertLast(0)
    param_3 = obj.getFront()
    param_4 = obj.insertLast(3)
    param_5 = obj.getFront()
    param_6 = obj.insertFront(9)
    param_7 = obj.getRear()
    param_8 = obj.getFront()
    param_9 = obj.getFront()
    param_10 = obj.deleteLast()
    param_11 = obj.getRear()
    print('queue: ', obj.queue, ' front: ', obj.front, ' rear: ', obj.rear)
