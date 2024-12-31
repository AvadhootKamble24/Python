lst=["banana","kiwi","mango","dragon"]
# lst1=[]
# for x in lst:
#     if "i" in x:
#         lst1.append(x)
#to make this code short list cimprihension can be used
lst1=[x for x in lst if "i" in x]
print(lst1)
lst2=[x for x in lst]
print(lst2)
lst3=[x for x in range(3,10)]
print(lst3)
lst4=[x.upper() for x in lst ]
print(lst4)
lst5=[x if x !="banana" else "orange" for x in lst]
print(lst5)