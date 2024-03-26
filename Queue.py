class Queue:
    def __init__(self) -> None:
        self.mylist = []

    def equeue(self, data):
        self.mylist.append(data)

    def is_empty(self):
        return len(self.mylist) == 0
    
    def dqueue(self):
        if not self.is_empty():
            self.mylist.pop(0)
        else:
            raise IndexError("Empty Queue")

    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            raise IndexError("Empty Queue")
    
    def get_rear(self):
        if not self.is_empty(self):
            return self.mylist[-1]
        else:
            raise IndexError("Empty Queue")
    def size(self):
        return len(self.mylist)

q1 = Queue()
# print(f"the item is {q1.get_front()}")
q1.equeue(10)
q1.equeue(20)
q1.equeue(30)
print(f"the item is {q1.get_front()}")
q1.dqueue()
print(f"the item is {q1.get_front()}")