# def selectionSort(lst):
#     n=len(lst) 
#     for i in range(n):
#         min_idx=i
#         for j in range(i+1,n):
#             if lst[j]<lst[min_idx]:
#                 min_idx= j
        
#         lst[i], lst[min_idx] = lst[min_idx],lst[i]

# lst = [29, 14, 73, 41, 66, 42, 5, 19]
# print (f"unsorted list={lst}")
# selectionSort(lst)
# print(f"sorted list={lst}")

def selectionSort(lst):
    n=len(lst)
    for i in range (n):
        min_idx=i
        for j in range(i+1,n):
            if lst[j]<lst[min_idx]:
                min_idx=j
        
        lst[i], lst[min_idx]=lst[min_idx], lst[i]

lst = [29, 14, 73, 41, 66, 42, 5, 19]
print (f"unsorted list={lst}")
selectionSort(lst)
print(f"sorted list={lst}")