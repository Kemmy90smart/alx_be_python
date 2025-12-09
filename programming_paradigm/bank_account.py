class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # Print as integer if whole number, otherwise print float
        bal = float(self.account_balance)
        if bal.is_integer():
            print(f"Current Balance: ${int(bal)}")
        else:
            print(f"Current Balance: ${bal}")
