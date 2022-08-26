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
        newNd = self.list.insertAfter(data, pageNum)

        node = newNd.getNext()
        while node is not None:
            node.pageNumber += 1
            node = node.getNext()

    def edit_page(self, pageNum, content):
        node = self.list.getNode(pageNum)
        node.setData(content)

    def get_next(self):
        if self.currNd == self.list.tail:
            print("you are already on the last page.\n")
            return

        self.currNd = self.currNd.getNext()
        print('\n--------PAGE---------')
        print(self.currNd)
        print()
        return self.currNd

    def get_prev(self):
        if self.currNd == self.list.head:
            print("\nyou are already on the first page.\n")
            return

        self.currNd = self.currNd.getPrev()
        print('\n--------PAGE---------')
        print(self.currNd)
        print()
        return self.currNd

    def __str__(self):
        return f'\n**Journal Name: {self.name}** {self.list}'
