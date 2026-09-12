from CurrentAccount import CurrentAccount
from FixedDepositAccount import FixedDepositAccount
from SavingsAccount import SavingsAccount
from Withdrawable import Withdrawable


def demonstrate_lsp_safe_withdrawals():
    accounts = [
        SavingsAccount(101, "Ravi", 500),
        CurrentAccount(202, "Maya", 1000),
        FixedDepositAccount(303, "Nisha", 2000),
    ]

    # Withdrawal operations use only the Withdrawable contract.
    withdrawable_accounts = [
        account for account in accounts if isinstance(account, Withdrawable)
    ]

    for account in withdrawable_accounts:
        account.withdraw(100)

    # FixedDepositAccount is deliberately not in withdrawable_accounts.
    return accounts


if __name__ == "__main__":
    demonstrate_lsp_safe_withdrawals()
