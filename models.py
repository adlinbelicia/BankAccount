class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"Amount deposited: {amount}"
    def withdraw(self, amount):
        self.balance -= amount
        return f"Amount withdrawn: {amount}"
    def get_balance(self):
        return self.balance
    def get_account_info(self):
        return f"=====Your Account Info=====\nAccount number: {self.account_number}\nAccount holder: {self.account_holder}\nAvailable balance: {self.balance:}\n==========================="
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return f"Interest amount: {interest_amount:}\n==========================="
