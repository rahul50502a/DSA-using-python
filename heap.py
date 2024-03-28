class Heap:
    def __init__(self) -> None:
        self.heap = []

    def createHeap(self, list1):
        for e in list1:
            self.insert(e)

    def insert(self, e):
        index = len(self.heap)
        parent_index = (index-1)//2
        while index > 0 and self.heap[parent_index]<e:
            if index == len(self.heap):
                self.heap.append(self.heap[parent_index])
            else:
                self.heap[index]=self.heap[parent_index]
            index = parent_index
            parent_index=(index-1)//2
        if index == len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    
    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        else:
            return self.heap[0]

    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            self.heap.pop()
        max_val = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftchildindex = 2*index + 1
        rigtchildindex = 2*index + 1
        while leftchildindex<len(self.heap):
            if rigtchildindex<len(self.heap):
                if self.heap[leftchildindex] > self.heap[rigtchildindex]:
                    if self.heap[leftchildindex] < temp:
                        self.heap[index] = self.heap[leftchildindex]
                        index = leftchildindex
                    else:
                        break
                else:
                    if self.heap[rigtchildindex] > temp:
                        self.heap[index] = self.heap[rigtchildindex]    
                        index=rigtchildindex
                    else:
                        break
            else: #No right child
                if self.heap[leftchildindex]>temp:
                    self.heap[index]=self.heap[leftchildindex]
                else:
                    break
            leftchildindex = 2*index + 1
            rigtchildindex = 2*index + 1
            return max_val
    def heapSort(self, list1):
        self.createHeap(list1)
        list2 = []
        try:
            while True:
                list2.insert(0, self.delete())
        except EmptyHeapException:                
            pass
        return list2
    
class EmptyHeapException(Exception):
    def __init__(self, msg="Empty Heap"):
        self.msg = msg

    def __str__(self):
        return self.msg