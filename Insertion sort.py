def inserstion_sort(list1):
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i-1
        while j>=0 and temp < list1[j]:
            list1[j+1]=list1[j]
            j -= 1
        list1[j+1]=temp
mylist=[25,37,11,14,60,82,18,41]
inserstion_sort(mylist)
print(mylist)
