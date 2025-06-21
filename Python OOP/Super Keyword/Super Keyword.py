#inheriting constructor
class Phones:
    def __init__(self,price,brand,camera):
        print("inheriting constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("HELLLLLOOOOOOOO")


class SmartPhones(Phones): #inheritance Smartphones(Child) is subclass of Phone(parents)
    def buy(self): #method overriding which is a kind of Polymorphism 
        print("HELLLLLOOOOOOOO World")
        super().buy()


customer=SmartPhones(1000,"iPhone","12mpx")
print(customer.buy())

