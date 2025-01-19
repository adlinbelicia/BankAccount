from models import SavingsAccount

# Create a new saving account
bank_account = SavingsAccount("14061999", "Chou Tzuyu", 1000000, 0.1)

# Perform actions
print(f"Hello {bank_account.account_holder}, here's your saving account data!")
print(bank_account.get_account_info())
print(bank_account.deposit(500))
print(bank_account.withdraw(500))
print(bank_account.calculate_interest())

# Current balance after interest
print("Total current balance with the interest: ", bank_account.get_balance())
