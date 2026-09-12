from Depositable import Depositable
from Withdrawable import Withdrawable


class ATM(Depositable, Withdrawable):

    def __init__(self, cash=0.0):
        self.cash = cash

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.cash += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.cash:
            return False

        self.cash -= amount
        return True
