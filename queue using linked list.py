class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None
    
    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
        self.item_count += 1
    
    def dqueue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear :
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count 