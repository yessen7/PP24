class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} tenge. New balance: {self.balance} tenge.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} tenge. New balance: {self.balance} tenge.")


account = BankAccount("Yessen", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)  # This withdrawal should be canceled due to insufficient funds.
account.deposit(300)
account.withdraw(400)
