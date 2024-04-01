class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


def insert_at_last(data):
    n = Node()


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_al_last(self, data):
        temp = self.start
        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next

        n = Node(temp, data, None)
        if temp is None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node()