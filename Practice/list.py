# Lists: Write a program that takes 5 numbers as input, stores them in a list, and then prints the largest and smallest number in the list.
lst=[]
for i in range (5):
    num=int(input('Enter number to add to list: '))
    lst.append(num)

print("Largest number:", max(lst))
print("Smallest number:", min(lst))