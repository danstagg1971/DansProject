class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        print(amount + self.balance)

    def withdraw(self, amount):
        print(self.balance - amount)

    def get_balance(self):
        print(self.balance)

    def display_info(self):
        print(f"Accout Number: {self.account_number}\nAccount name: {self.account_holder}\nBalance: {self.balance}")


account1 = BankAccount("12345", "Dan Stagg", 1500)
account2 = BankAccount("2468", "Paul Simon", 500)

account1.deposit(500)
account1.withdraw(500)

account2.deposit(100.0)
account2.withdraw(700.0)

account1.display_info()
account2.display_info()
