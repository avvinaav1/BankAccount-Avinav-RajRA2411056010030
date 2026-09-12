from FixedDepositAccount import FixedDepositAccount
from SavingsAccount import SavingsAccount


def demonstrate_violation():
    accounts = [
        SavingsAccount(101, "Ravi", 500),
        FixedDepositAccount(202, "Maya", 1000),
    ]

    # This loop models the QA failure: the Fixed Deposit crashes the iteration.
    for account in accounts:
        account.withdraw(100)


if __name__ == "__main__":
    demonstrate_violation()
