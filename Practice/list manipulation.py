# List Manipulation: Write a program that takes a list of integers and removes all duplicates, then sorts the list in descending order.

lst=[]
while(True):
    choice=int(input('*Menu*\n1.Add number to list\n2.Exit'))
    if choice==1:
        num=int(input('Enter number: '))
        lst.append(num)
    if choice==2:
        break

print('List with duplicates',lst)
lst=list(set(lst))
print('List with duplicates',lst)
