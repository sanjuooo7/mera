class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Current balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.balance}"
        
    def display_balance(self):
        return f"Account Number: {self.account_number}\nAccount Holder:{self.account_holder_name}\nCurrent Balance: ${self.balance}"


# Demonstrate the functionality
account1 = BankAccount("123456789", "John Doe", 1000.0)
print(account1.display_balance())
print(account1.deposit(500.0))
print(account1.withdraw(200.0))
print(account1.display_balance())
