#The Equality operator (==) is a comparison operator in Python that compare values of both the operands and checks for value equality. Whereas the 'is' operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).

a=10
b=10
if( a == b ):
    print("Equality Operator")

print(id(a))
print("<------------->")
print(id(b))
print("<------------->")

#"is" operator checks weather 2 operands refer same object or not.(Same memory location)
print( a is b )

print("<--------------------->")
list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

print(id(list1))
print(id(list2))
print(id(list3))