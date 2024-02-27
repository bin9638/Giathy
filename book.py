#Yêu Hân Ly vcl <33333
class BankAccount:
    def __init__(self, account_number, account_owner, balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance
        assert account_number > 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} SGD added to your account {self.account_number}. Current balance: {self.balance} SGD."
        else:
            return "The amount deposited into the account must be greater than 0 SGD."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"{amount} SGD has been withdrawn from the account {self.account_number}. Current balance: {self.balance} SGD."
        else:
            return "Invalid withdrawal amount or insufficient balance in the account."

    def check_balance(self):
        return f"Balance in account {self.account_number}: {self.balance} SGD."

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.account_list = {}

    def add_account(self, account_number, account_owner):
        bank_account = BankAccount(account_number, account_owner)
        self.account_list[account_number] = bank_account
        return f"Account {account_number} has been created for {account_owner}."

    def get_account(self, account_number):
        if account_number in self.account_list:
            return self.account_list[account_number]
        else:
            return "Account does not exist."

# Example usage:
user = User("John Doe")
print(user.add_account("12345", "Alice"))
print(user.add_account("67890", "Bob"))

alice_account = user.get_account("12345")
bob_account = user.get_account("67890")

print(alice_account.deposit(1000))
print(alice_account.check_balance())
print(bob_account.withdraw(500))
print(bob_account.check_balance())