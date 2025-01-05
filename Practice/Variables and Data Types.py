# Variables and Data Types: Write a program that takes user input for their name and age, 
# then prints a greeting message with their name and calculates how many years it will take for them to turn 100.

name=input('Enter your name: ')
age=int(input("Enter your age: "))
yrs_till_100= 100-age

print(f"Good Morning {name} \n You will turn 100 after {yrs_till_100} years ")
