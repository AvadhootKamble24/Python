'''
Dictionary Manipulation: Write a program that reads a paragraph of text and returns a dictionary 
where the keys are words, and the values are the frequency of those words in the text.
'''

para=input('Enter a paragraph:\n')

lst=para.split()


dict={}

count=1
for i in range(len(lst)):
    if lst[i] not in dict:
        dict[lst[i]]=count
    else:
        dict[lst[i]]=count+1
print(dict)