# num=input("Enter number:")

# try:
#     num=float(num)
#     print("Number is: ",num)
# except:
#     print("invalid number")

datavalidate = False
while datavalidate==False:
    grade1=input("Enter grade1:")
    if grade1<0 or grade1 >10:
        print("Enter grade between 1-10 only")
        continue
    else:
            datavalidate=True
datavalidate = False
while datavalidate==False:
    grade2=input("Enter grade1:")
    if grade2<0 or grade2 >10:
        print("Enter grade between 1-10 only")
        continue
    else:
            datavalidate=True

datavalidate = False
while datavalidate==False:
     totalClasses=input("Enter total number of classes")
     if totalClasses<=0:
          print("Total number of classes cannot be less than 0")
          continue
     else:
          datavalidate=True