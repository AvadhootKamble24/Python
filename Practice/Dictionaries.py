# Dictionaries: Create a dictionary with 5 key-value pairs 
# (representing 5 countries and their capitals). Write a program to print all 
# countries and their capitals and allow the user to input a country to get its capital.

countries={'india':'delhi','australia':'canberra','russia':'moscow','united kingdom':'london','italy ':'rome'}
print(countries)

country=input('Enter name of country to know their capital: ').lower()
print(countries[country])