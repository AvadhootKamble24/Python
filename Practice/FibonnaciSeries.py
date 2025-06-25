# Brut solution

def fib(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a,b=b,c
        print(c)

fib(5)
print('~~~~')

# Recursssion Soluiton

def fibo(n):
    if n==0:return 0
    if n==1:return 1
    return fibo(n-1)+fibo(n -2)
n=5
for i in range (n):
    print(fibo(i)) 