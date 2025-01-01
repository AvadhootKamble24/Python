# how to define a class
class human:
    def __init__(self, name,age):
        self.name = name
        self.age =age
    
    def methods(self):
        print("Hi I'm " + self.name+ " I'm " +str(self.age)+" years old.")

# how to declare an object
h1= human("avadhoot",20)
# print(h.name)
# print(h.age)

h1.methods()
h2 = human("avanee",11)
h2.methods()
h2.age=16
h2.name="sakshi"
h2.methods()