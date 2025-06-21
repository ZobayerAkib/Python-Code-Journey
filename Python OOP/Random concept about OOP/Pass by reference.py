class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

#<==========================================================>
def greet(Customer): #reference of x or y which is an object of customer class
    if(Customer.gender=="Male"):
        print(f"Hello {Customer.name} sir")
    else:
        print(f"Hello {Customer.name} ma'am")
#<==========================================================>
x=Customer("Akib","Male")
y=Customer("Kiara","Female")

greet(x)
greet(y)
