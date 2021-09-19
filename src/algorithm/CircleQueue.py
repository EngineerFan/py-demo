# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2021/6/27 12:57
# @Software    : PyCharm
# @Description :

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.length = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        qLength = len(self.q)
        if qLength == 0:
            self.q.append(value)
            self.head , self.tail = 0 , 0
            return True
        else:
            if self.tail + 1 < self.length:
                self.q.append(value)
                self.tail = self.tail + 1
                return True
            else:
                return False



    def deQueue(self) -> bool:
        qLength = len(self.q)
        if qLength != 0:
            self.q.pop(self.head)
            self.tail -= 1
            if len(self.q) == 0:
                self.head = -1
                self.tail = -1
            return True
        else:
            return False


    def Front(self) -> int:
        if len(self.q) == 0:
            return -1
        else:
            return self.q[self.head]

    def Rear(self) -> int:
        if len(self.q) == 0:
            return -1
        else:
            return self.q[self.tail]

    def isEmpty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.tail == self.length - 1:
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()