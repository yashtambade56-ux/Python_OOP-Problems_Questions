# Create a BankAccount class with deposit, withdraw, and balance check.

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money!")

    def check(self):
        print("Balance:", self.balance)

# Example usage
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.check()
account.withdraw(600)  # This should print "Not enough money!"