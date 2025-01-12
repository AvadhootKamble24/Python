# def bubbleSort(lst):
#     n= len(lst)

#     for i in range(n):
#         swapped= False
#         for j in range(0,n-i-1):
#             if lst[j]>lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#                 swapped = True

#         if not swapped:
#             break


def bubbleSort(lst):
    n=len(lst)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1]= lst[j+1], lst[j]
                swapped=True
        if not swapped:
            break

lst = [29, 14, 73, 41, 66, 42, 5, 19]
print (f"unsorted list={lst}")
bubbleSort(lst)
print(f"sorted list={lst}")
