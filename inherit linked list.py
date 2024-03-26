from assign3 import *
class Stack(SLL):
    def __init__(self, start=None):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(Self):
        if not Self.is_empty():
            Self.delete_first()
            Self.item_count -= 1
        else:
            raise IndexError("Stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack underflow")    
    
    def size(self):
        return self.item_count
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(f"Top element on the stack is {s1.peek()}")
s1.pop()
print(f"Top element on the stack is {s1.peek()}")