from AccountRepository import AccountRepository
from BankAccount import BankAccount
from NotificationService import NotificationService
from SavingsInterestPolicy import SavingsInterestPolicy
from StatementGenerator import StatementGenerator


def main():

    account = BankAccount(101, "Ravi", 500)

    account_repository = AccountRepository()
    notification_service = NotificationService()
    statement_generator = StatementGenerator()
    interest_policy = SavingsInterestPolicy()

    if account.deposit(1000):
        notification_service.send(
            "Deposit completed for account "
            + str(account.get_account_number())
        )
        account_repository.save(account)

    if account.withdraw(500):
        notification_service.send(
            "Withdrawal completed for account "
            + str(account.get_account_number())
        )
        account_repository.save(account)

    print(statement_generator.generate(account))
    print(
        "Interest earned: Rs. "
        + str(interest_policy.calculate(account.get_balance()))
    )


if __name__ == "__main__":
    main()
