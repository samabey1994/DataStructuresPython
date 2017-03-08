def bubbleSort(lst):
    for i in range(0,len(lst)-1):
        for j in range(0,len(lst)-1-i):
            if(lst[i]>lst[i+1]):
                lst[i],lst[i+1] = lst[i+1], lst[i]
    return lst

print(bubbleSort([2, 9, 10, 15, 25, 16]))
