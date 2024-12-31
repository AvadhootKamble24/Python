# Variables and Data Types
a=10
b="avadhoot"
c=True
d=125.56
print(a,b,c,d ,sep=',')
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# concatenate
print(str(a)+b)

# data types
# numeric = int float complex
e=234
f=268.364
g=45+6j
print(type(g))

# list,tuple
lst=[1,2,"ack",21.5,['a','v','c','b'],True] #mutable
tuple=(1,2,"ack",21.5,['a','v','c','b'],True) #immutable
print(lst ,'\n',tuple)
print()
# dictionary
info={'name':'avk','age':21, 'address':'pune'}

print(info)
print(info.values())
