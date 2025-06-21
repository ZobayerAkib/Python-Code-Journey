class ShoppingCart:

    def __init__(self):
        self.items=[]
        self.sum=0
        self.menu()
    def menu(self):
        user_input = input(
            """
         Hello! please select any option:
         <===============================>
         Press 1 for add item
         <===============================>
         Press 2 for remove item
         <===============================>
         Press 3 for Calculate Total
         <===============================>
         Press 4 for display items
         <===============================>
         Press 5 for display exit
         <===============================>
         Enter any option: """)
        if user_input == "1":
            self.add_item()
        elif user_input == "2":
            self.remove_item()
        elif user_input == "3":
            self.calculate_total()
        elif user_input == "4":
            self.display_item()
        else:
            print("Bye, Thank You!")

    def add_item(self):
        item_name = input("Enter the item name: ")
        qty=int(input("Enter the qty: "))
        item=(item_name,qty)
        self.items.append(item)
        self.menu()

    def remove_item(self):
        item_name=input("Enter the item name: ")
        for x in self.items:
            if x[0]==item_name:
                self.items.remove(x)
                break
            else:
                print("Item not found!")
        self.menu()

    def calculate_total(self):

        for x in self.items:
            self.sum+=x[1]
        print(f"The total quantity is : {self.sum}")
        self.menu()

    def display_item(self):
        for x in self.items:
            print(f"{x[0]}:{x[1]}")
        self.menu()

customer=ShoppingCart()







