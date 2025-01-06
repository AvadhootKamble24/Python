'''	
List Slicing and Advanced Indexing: Write a program that takes a list and rotates 
it to the right by n positions (without using any built-in function).
'''

lst=[1,2,3,4,5]
print(lst)
lst2=[]
n=3
split=len(lst)-n
for i in range (0,len(lst)):
    while i ==split:
        print(i)
        lst2.append(lst[i])
        lst.pop(lst[i])
        i+=1
        continue
print(lst2)