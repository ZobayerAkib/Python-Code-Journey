class ATM:
    #static/ class variable
    """
    In Python, a static variable, also known as a class variable,
    is a variable shared among all instances of a class.
    It is defined within the class but outside of any methods
    and is accessed using the class name or an instance of the class.
    Class variables are suitable for maintaining information that is common to all instances of a class,
    such as a counter or a list of all created instances.

    """
    __serial_number=1 #private variable
    def __init__(self):
        #instance variable
        self.__pin="" #private variable
        self.name=""
        self.__balance=0 #private variable
        self.menu()
        ATM.__serial_number=ATM.__serial_number+1

    def menu(self):
        user_input=input(
           """
        Hello! please select any option:
        <===============================>
        Press 1 for create Pin
        <===============================>
        Press 2 for Deposit
        <===============================>
        Press 3 for Withdraw
        <===============================>
        Press 4 for Check Balance
        <===============================>
        Press 5 for Exit
        <===============================>
        Enter any option: """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Bye, Thank You!")

    def create_pin(self):
        self.name = input("Enter your name: ")
        self.__pin=input("Enter your pin: ")

        print("<===============================>")
        print("Pin set successfully!")
        print("<===============================>")
        self.menu()

    # ---------------------------------------------------------
    @staticmethod
    def get_Sno():
        return ATM.__serial_number

    # ---------------------------------------------------------

    @staticmethod
    def set_Sno(new):
        if type(new) == int:
            ATM.__serial_number = new
        else:
            print("Not allowed!")

    # ---------------------------------------------------------
    def get_pin(self):
        return self.__pin

    # ---------------------------------------------------------
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin changed")
        else:
            print("Not allowed!")

    def deposit(self):
        pid=input("Enter your pin: ")
        print("<===============================>")
        if pid==self.__pin:
            print(f"Serial Number: {ATM.__serial_number}")
            print(f"Account Name: {self.name}")
            amount=int(input("Enter the amount: "))
            print("<===============================>")
            self.__balance=self.__balance+amount
            print("Deposit successfully!")
            print("<===============================>")
        else:
            print("Wrong pin, Enter the pin again! ")
            print("<===============================>")
        self.menu()

    # ---------------------------------------------------------

    def withdraw(self):
        pid = input("Enter your pin: ")
        print("<===============================>")
        if pid == self.__pin:
            print(f"Serial Number: {ATM.__serial_number}")
            print(f"Account Name: {self.name}")
            amount = int(input("Enter the amount: "))
            print("<===============================>")
            if amount<=self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw successfully!")
                print("<===============================>")
            else:
                print("Insufficient Balance!")
                print("<===============================>")

        else:
            print("Wrong pin, Enter the pin again! ")
            print("<===============================>")
        self.menu()

    #---------------------------------------------------------

    def check_balance(self):
        pid = input("Enter your pin: ")
        print("<===============================>")
        if pid == self.__pin:
            print(f"Serial Number: {ATM.__serial_number}")
            print(f"Account Name: {self.name}")
            print(f"The amount is {self.__balance}")
            print("<===============================>")
        else:
            print("Wrong pin, Enter the pin again! ")
            print("<===============================>")
        self.menu()

if __name__ == '__main__':
    ebl=ATM()

    #print(ebl.get_Sno())






