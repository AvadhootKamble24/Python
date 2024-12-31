#working with list
#list can contain multiple datatype at once
friends = ["sakshi","aditi","manasi","raj","sania","shrutika"] #list named friends

print(friends) #prints whole list
print("-----------------------------------------------")

print(friends[0]) #prints element at given index

friends[3] = "avadhoot" #updateds value at given ndex
print("-----------------------------------------------")
print(friends)

#functions in list
friends.append("krutika") #append add vale at the end of listprint
print("-----------------------------------------------")
print(friends)

luckey_numbers =[2,4,3,7,56,34,76]
friends.extend(luckey_numbers) #concat 2 lists
print("-----------------------------------------------")
print(friends)
friends.insert(3,"raj") #inserts element at given index and pushes index values next to it
print("-----------------------------------------------")
print(friends)
friends.remove("avadhoot") #removes passed element
print("-----------------------------------------------")
print(friends)
friends.clear()#clears all list
print("-----------------------------------------------")
print(friends)
friends = ["sakshi","aditi","manasi","raj","sania","shrutika"] #list named friends
friends.pop() #removes last element
print("-----------------------------------------------")
print(friends)
print("-----------------------------------------------")
print(friends.index("sakshi")) #prints index of passed element
friends.append("avadhoot")
friends.append("avadhoot")
print("-----------------------------------------------")
print(friends.count("avadhoot"))
friends.sort()   
print("-----------------------------------------------")
print(friends)
luckey_numbers.sort()#sorts list in ascending order
print("-----------------------------------------------")
print(luckey_numbers)
luckey_numbers.reverse()
print(luckey_numbers)
friends2 = friends.copy()
print(friends2)

nums=[1,3,4,5,7,5345,7]
friends.extend(nums)
print(friends)