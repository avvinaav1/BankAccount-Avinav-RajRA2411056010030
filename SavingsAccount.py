from BankAccount import BankAccount
from Depositable import Depositable
from StatementGenerator import StatementGenerator
from StatementProvider import StatementProvider
from Transferable import Transferable
from Withdrawable import Withdrawable


class SavingsAccount(
    BankAccount,
    Depositable,
    Withdrawable,
    Transferable,
    StatementProvider,
):

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )
        return True

    def transfer(self, target, amount):
        if not self.withdraw(amount):
            return False

        return target.deposit(amount)

    def print_statement(self):
        return StatementGenerator().generate(self)
