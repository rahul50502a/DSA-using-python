class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item= item
        self.next = next

class CDLL:
    def __init__(self, start=None) -> None:
        self.start = start
        
    def is_empty(self):
        return self.start == None

    def insertatstart(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

        self.start = n

    def insertatlast(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
    def search(self, data):
        temp = self.start
        if self.start == None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    
    def insertafter(self, temp, data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end='')
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end='')
                temp = temp.next

    def delete_first(self):
        if self.satrt != None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next 
                self.start.next.prev = self.start.prev
                self.start = self.start.next
        
    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    
    def delete_item(self, data):
        if self.start is not None:
            if self.start.next == self.start: 
                if self.start.item == None:
                    self.start = None
            else:
                temp = self.start
                

                