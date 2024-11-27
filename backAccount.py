class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def __str__(self):
        return f"{self.account_holder} has {self.balance} in the account"

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
        else:
            print("Account is closed")

    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Account is closed")

    def deactivate(self):
        self.is_active = False
        print("Account is closed")

    def activate(self):
        self.is_active = True
        print("Account is open")


account1 = BankAccount("Alice", 100)
account2 = BankAccount("Bob", 200)

account1.deposit(50)
account2.withdraw(50)
print(account1)
print(account2)

account1.deactivate()
account1.withdraw(50)
print(account1)

account1.activate()
account1.deposit(250)
print(account1)
