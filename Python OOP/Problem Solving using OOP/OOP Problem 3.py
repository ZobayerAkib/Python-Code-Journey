"""
Encapsulation - Protecting Attributes: Implement a class Account with a private attribute balance
and provide methods to deposit and withdraw safely, checking for sufficient funds.
"""
class Account:

    def __init__(self):
        self.__balance=0
        self.menu()

    def menu(self):
        user_input=input("""
            press 1 for deposit.
            press 2 for withdraw.
            press 3 for check fund.
            press 4 for exit.
            Enter the option: 
            
        """)
        if user_input=="1":
            self.deposit()
        elif user_input=="2" :
            self.withdraw()
        elif user_input=="3":
            self.check_fund()
        else:
            print("Bye, Thank You !")

    def deposit(self):
        balance=int(input("Enter the amount: "))
        self.__balance=self.__balance+balance
        print("Deposit successfully!")
        self.menu()
    def withdraw(self):
        balance = int(input("Enter the amount: "))
        if balance <= self.__balance:
            self.__balance = self.__balance + balance
            print("Withdraw successfully!")
        else:
            print("Insufficient balance! ")
        self.menu()
    def check_fund(self):
        print(f"The remaining amount is: {self.__balance}")
        self.menu()

customer=Account()
