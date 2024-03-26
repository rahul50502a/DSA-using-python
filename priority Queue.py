class PriorityQueue:
    def __init__(self):
        self.item = []

    def push(self, data, priority):
        index = 0
        while index < len(self.item) and self.item[index][1] <= priority:
            index += 1
        self.item.insert(index, (data, priority))

    def is_empty(self):
        return len(self.item) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("priority Queue is empty")
        return self.item.pop(0)[0]

    def size(self):
        return len(self.item)