# Reasons the original class may need to change:
# 1. Account-operation rules change (deposit, withdrawal, or balance rules).
# 2. Customer and account validation rules change.
# 3. PIN or account-status security rules change.
# 4. Interest-rate policy changes.
# 5. The database or persistence mechanism changes.
# 6. The email provider or notification format changes.
# 7. The statement or transaction-log format changes.
#
# BankAccount job description: Manage deposits, withdrawals, and the account balance, and expose simple account data.


class BankAccount:

    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transaction_log = []

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )
        return True

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_transaction_log(self):
        return list(self.transaction_log)
