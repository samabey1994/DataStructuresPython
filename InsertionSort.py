def insertionSort(lst):
    for i in range(1, len(lst)):
        x = lst.pop(i)
        for j in range(0, i):
            if(lst[i-j-1]<x):
                lst.insert(i-j, x)
                break
            elif(j==i-1):
                lst.insert(0, x)
    return lst
print(insertionSort([2, 9, 10, 15, 25, 16]))
