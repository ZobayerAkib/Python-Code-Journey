#inheriting constructor
#super keyword


class Phones:
    def __init__(self,price,brand,camera):
        print("inheriting constructor")
        self.price=price
        self.brand=brand
        self.camera=camera



class SmartPhones(Phones): #inheritance Smartphones(Child) is subclass of Phone(parents)
    def __init__(self, price, brand, camera,os,ram):
        print("smartphone")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram


customer=SmartPhones(1000,"iPhone","12mpx","ios",12)
print(customer.os)

