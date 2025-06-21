# has a relation type is aggregation
class Customer:
    def __init__(self,address,gender,name):
        self.address=address
        self.gender=gender
        self.name=name

class Address:
    def __init__(self,area_name,pin_code,city):
        self.area_name=area_name
        self.pin_code=pin_code
        self.city=city

add=Address("Banasree","1219","Dhaka")
c1=Customer(add,"Male","Zobayer")
print(c1.address)
print(c1.address.area_name)
print(c1.address.pin_code)
print(c1.name)
