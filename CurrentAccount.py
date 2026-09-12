from BankAccount import BankAccount
from Withdrawable import Withdrawable


class CurrentAccount(BankAccount, Withdrawable):

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )
        return True
