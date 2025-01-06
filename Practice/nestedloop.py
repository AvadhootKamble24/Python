'''
Nested Loops: Write a program that generates a multiplication table (from 1 to 10) 
using nested loops, and formats it into a well-aligned table.
'''

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")