#inheriting constructor
class Phones:
    def __init__(self,price,brand,camera):
        print("inheriting constructor")
        self.price=price
        self.brand=brand
        self.camera=camera


class SmartPhones(Phones): #inheritance Smartphones(Child) is subclass of Phone(parents)
    pass


customer=SmartPhones(1000,"iPhone","12 mpx")
print(customer.brand)

