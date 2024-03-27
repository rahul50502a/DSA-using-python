def Quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x <= pivot]
        greater=[x for x in list1[1:] if x > pivot]
        return Quick_sort(lesser) + [pivot] + Quick_sort(greater)
    
mylist = [53,11,72,68,41,25,18,37,44,80]
mylist=Quick_sort(mylist)
print(mylist)