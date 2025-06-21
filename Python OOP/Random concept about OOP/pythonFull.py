#function and zip practice
def f(name, id):
    print("hi", name)
    print("id", id)

l=["a","b","c"]
l1=[1,2,3]

for x,y in zip(l,l1):
        f(x,y)
#==============================================================================#

#Parameter and Argument
def fn(name): #here name is parameter
    print(f"my name is {name}")

fn("Akib") #akib is  an argument
#==============================================================================#

"""
Types of arguments in Python
    1.Positional arguments

    2.Keyword arguments

    3.Default arguments

    4.Variable-length arguments
"""
#1
def Fn(name, id):
    print(f"my name is {name} and my id is {id}")

Fn("Akib",123)
#==============================================================================#
#2
def Fn(name, id):
    print(f"my name is {name} and my id is {id}")

Fn(id=123, name="Zobayer")
#==============================================================================#
#3

def fn(name="Md. Zobayer Ibna Kabir"):
    print(f"My name is {name}")

fn()
#==============================================================================#
#4.1
def fn(*number): #*args(Non Keyword Arguments) – for multiple positional arguments
    print("total sum is: ",sum(number))

fn(1,2,3,4,5)

def fn(*name):
    nm="Md. Zobayer "
    for x in name:
        nm= nm + x
    print("my name is: ",nm)
fn("Ibna ","Kabir ")
#==============================================================================#
#4.2

def print_info(**info): #**kwargs – for multiple keyword arguments
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Zobayer", age=24, country="Bangladesh")

#==============================================================================#
#map(function, iterable)

l=[1,2,3,4]
sqrNumber=list(map(lambda x: x*2 , l ))
print(sqrNumber)

#==============================================================================#
#filter(function, iterable)
l=[1,2,3,4]
isEvenNumber=list(filter(lambda x: x%2==0 , l ))
print(isEvenNumber)

#==============================================================================#
#Enumerate

l=[1,2,3,4,5]
for x, y in enumerate(l):
    print(f"{x}: {y}")



