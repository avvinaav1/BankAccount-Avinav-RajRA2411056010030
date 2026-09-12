class InterestCalculator:

    # To add a fourth account type in this closed design:
    # - Open this file and edit the calculate() method.
    # - Add another condition to the account_type if/elif chain.
    # - Add another return line containing the new interest rate.
    # Existing callers remain unchanged because they already pass type and balance.
    def calculate(self, account_type, balance):
        if account_type == "Savings":
            return balance * 0.04
        elif account_type == "Current":
            return balance * 0.01
        elif account_type == "Salary":
            return balance * 0.05
        else:
            return 0.0
