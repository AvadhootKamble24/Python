def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1								# key=3
        while j>=0 and key<arr[j]:		#-1	[14, __,  29, 41, 66, 42, 66, 73]
            arr[j+1]=arr[j]				#     j      key,i
            j-=1
        arr[j+1]=key
        
lst = [29, 14, 73, 41, 66, 42, 5, 19]
print (f"unsorted list={lst}")
insertionSort(lst)
print(f"sorted list={lst}")