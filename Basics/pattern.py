'''
to print 
* * * *
* * * *
* * * *
* * * *
'''
def prntpattern(n):
    for i in range (n):
        for j in range (n):
            print("*" ,end=" ")
        print()
prntpattern(5)
'''
to print 
*
* *
* * *
* * * *
'''
def prntpattern(n):
    for i in range (n):
        for j in range (i+1):
            print("*" ,end=" ")
        print()
prntpattern(5)
'''
to print 
* * * *
* * *
* * 
* 
'''
def prntpattern(n):
    for i in range (n):
        for j in range (i,n):
            print("*" ,end=" ")
        print()
prntpattern(5)

for i in range (0,5):
    print("*"*i ,end=" ")
    print()