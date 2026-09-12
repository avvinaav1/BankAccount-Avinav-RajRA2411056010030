class BankService:

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, target, amount):
        pass

    def print_statement(self):
        pass

    def apply_for_loan(self, amount):
        pass


class ATM(BankService):

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    # Forced by the fat interface, but an ATM does not need transfers.
    def transfer(self, target, amount):
        pass

    # Forced by the fat interface, but an ATM does not print statements.
    def print_statement(self):
        pass

    # Forced by the fat interface, but an ATM does not process loan applications.
    def apply_for_loan(self, amount):
        pass
