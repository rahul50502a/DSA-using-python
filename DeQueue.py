class DeQueue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def insert_front(self, data):
        self.items.insert(0, data)
        
    def insert_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Empty DeQueue")
        
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop(-1)
        else:
            raise IndexError("Empty DeQueue")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Empty Queue")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Empty Queue")