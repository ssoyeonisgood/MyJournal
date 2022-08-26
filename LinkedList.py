from Node import *


class LinkedList:
    def __init__(self, head=None, tail=None, maxLen=25):
        self.head = head
        self.tail = tail
        self.length = 0
        self.maxLen = maxLen

    def __iter__(self):
        currNd = self.head
        while currNd is not None:
            yield currNd.data
            currNd = currNd.next

    def __str__(self):
        string = ''
        value = self.head
        while value is not None:
            string += f'\n{value}'
            value = value.getNext()
        return string

    def isEmpty(self):
        return self.head == None

    def insertFirst(self, newData):
        if self.length >= self.maxLen:
            raise Exception("My journal is full")

        newNd = Node(newData, 1)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            self.head.setPrev(newNd)
            newNd.setNext(self.head)
            self.head = newNd
        self.length += 1

    def insertLast(self, newData):
        if self.length >= self.maxLen:
            raise Exception("My journal is full")

        newNd = Node(newData, self.length + 1)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            currNd = self.head
            while (currNd.getNext() != None):
                currNd = currNd.getNext()
            currNd.setNext(newNd)
            newNd.setPrev(currNd)
            self.tail = newNd
        self.length += 1
        print(newNd.getPrev())

    def insertAfter(self, newData, pageNum):
        if self.length >= self.maxLen:
            raise Exception("My journal is full")

        newNd = Node(newData, pageNum + 1)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            currNd = self.head
            for i in range(pageNum - 1):
                currNd = currNd.getNext()
            nextNd = currNd.getNext()
            currNd.setNext(newNd)
            newNd.setNext(nextNd)
            nextNd.setPrev(newNd)
            newNd.setPrev(currNd)
        self.length += 1
        return newNd

    def getNode(self, pageNum):
        currNd = self.head
        for i in range(pageNum - 1):
            currNd = currNd.getNext()
        return currNd

    def peekFirst(self):
        if self.isEmpty():
            return None
        else:
            value = self.head.getData()
            return value

    def peekLast(self):
        if self.isEmpty():
            return None
        else:
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext()
            lastPeek = currNd.getData()
            return lastPeek

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            value = self.head.getData()
            self.head = self.head.getNext()
            self.length -= 1
            return value

    def removeLast(self):
        if self.isEmpty():
            return None
        elif self.head.getNext() == None:
            value = self.head.getData()
            self.head = None
            self.length -= 1
        else:
            currNd = self.head
            while currNd.getNext() != None:
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            value = currNd.getData()
            self.length -= 1
            return value
