#merge sort
# def mergeSort(lst):
#     if len(lst)>1:
#         mid=len(lst)//2
#         l=lst[:mid]
#         r=lst[mid:]

#         mergeSort(l)
#         mergeSort(r)
#         i=j=k=0
#         while i < len(l) and j < len(r):
#             if l[i]<=r[j]:
#                 arr[k]=l[i]
#                 i+=1
#             else:
#                 arr[k]=r[j]
#                 j+=1
#             k+=1
#         while i<len(l):
#             arr[k]=l[i]
#             i+=1
#             k+=1
#         while j<len(r):
#             arr[k]=r[j]
#             j+=1
#             k+=1
# def printlst(lst):
#     for i in lst:
#         print(i,end=' ')
#     print()


def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1


arr = [12, 11, 13, 5, 6, 7]

mergeSort(arr)
print(arr)