class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def intro(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

c1=Customer("Akib",25)
c2=Customer("Zobayer",26)

l=[c1,c2]

for x in l:
    print(x.name,x.age)
    x.intro()