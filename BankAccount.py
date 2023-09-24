# Bank Account calculator
# This is for the new branch called Bank Calc Edit 1


class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    # fdsfdsjkfdsajfkd
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    # gfjdkigjfokidgjofdgofd
    def get_balance(self):
        print(self.balance)

    def display_info(self):
        print(f"Account Number: {self.account_number}\nAccount name: {self.account_holder}\nBalance: {self.balance}")


account1 = BankAccount("12345", "Dan Stagg", 1500)
account2 = BankAccount("2468", "Paul Simon", 500)

account1.deposit(500)
account1.withdraw(500)

account2.deposit(100.0)
account2.withdraw(700.0)

account1.display_info()
account2.display_info()
