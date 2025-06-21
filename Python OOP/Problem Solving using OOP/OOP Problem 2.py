"""
Car Class: Create a Car class with attributes make, model, and year.
Include a method to display the details of the car.
"""
class Car:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.display_details()

    def display_details(self):

        print(f"The model of the car is: {self.model}, and launching year is: {self.year} and Make: {self.make}")


BMW=Car('BMW ',"series I-8",2025)