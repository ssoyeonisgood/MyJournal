class Node:
    def __init__(self, data, pageNumber=0):
        self.data = data
        self.next = None
        self.prev = None
        self.pageNumber = pageNumber

    def __str__(self):
        return f'data: {self.data} pageNumber: {self.pageNumber}'

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        return self.prev is prev
