from LinkedList import*


class Journal:
    def __init__(self, name):
        self.name = name
        self.list = LinkedList()
        self.currNd = None

    def add_page_front(self, data):
        node = self.list.head
        while node is not None:
            node.pageNumber += 1
            node = node.getNext()
        self.list.insertFirst(data)
        self.currNd = self.list.head

    def add_page_last(self, data):
        self.list.insertLast(data)

    def add_page_middle(self, data, pageNum):
        newNd = self.list.insertMiddle(data, pageNum)

        node = newNd.getNext()
        while node is not None:
            node.pageNumber += 1
            node = node.getNext()

    def pickData(self, pageNum, content):
        if self.list.isEmpty():
            return None
        else:
            node = self.list.head
            while node is not None:
                if node.pageNumber == pageNum:
                    content = node.getData()
        return content

    def __str__(self):
        return f'\nName: {self.name} \nList: {self.list}'
