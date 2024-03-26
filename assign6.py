class Stack:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return len(self.item) == 0
    
    def push(self, data):
        self.item.appen(data)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndentationError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndentationError("Stack is empty")
    def size(self):
        return len(self.item)