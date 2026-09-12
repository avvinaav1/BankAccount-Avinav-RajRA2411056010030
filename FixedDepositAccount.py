from BankAccount import BankAccount


class UnsupportedOperationException(Exception):
    pass


class FixedDepositAccount(BankAccount):

    def withdraw(self, amount):
        raise UnsupportedOperationException(
            "Fixed deposits cannot be withdrawn early"
        )
