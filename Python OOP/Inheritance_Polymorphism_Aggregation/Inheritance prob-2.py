#Inheriting private members: private attributes or members cannot be inherited.
#inheriting constructor
class Phones:
    def __init__(self,price,brand,camera):
        print("inheriting constructor")
        self.price=price
        self.__brand=brand
        self.camera=camera


class SmartPhones(Phones): #inheritance Smartphones(Child) is subclass of Phone(parents)
    pass


customer=SmartPhones(1000,"iPhone","12 mpx")
print(customer.__brand) #output: AttributeError: 'SmartPhones' object has no attribute '__brand'

