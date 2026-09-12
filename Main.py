from AccountRepository import AccountRepository
from Bank import Bank
from ConsoleNotificationService import ConsoleNotificationService
from FileAccountRepository import FileAccountRepository
from SavingsAccount import SavingsAccount
from SavingsInterestPolicy import SavingsInterestPolicy
from StatementGenerator import StatementGenerator


def main(notification_service, account_repository: AccountRepository):

    bank = Bank(notification_service, account_repository)
    account = SavingsAccount(101, "Ravi", 500)

    statement_generator = StatementGenerator()
    interest_policy = SavingsInterestPolicy()

    bank.deposit(account, 1000)
    bank.withdraw(account, 500)

    print(statement_generator.generate(account))
    print(
        "Interest earned: Rs. "
        + str(interest_policy.calculate(account.get_balance()))
    )


if __name__ == "__main__":
    main(
        ConsoleNotificationService(),
        FileAccountRepository("accounts.txt"),
    )
