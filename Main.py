from AccountRepository import AccountRepository
from Bank import Bank
from NotificationService import NotificationService
from SalaryAccount import SalaryAccount
from SalaryInterestPolicy import SalaryInterestPolicy
from StatementGenerator import StatementGenerator


def main(notification_service):

    bank = Bank(notification_service)
    account = SalaryAccount(101, "Ravi", 500)

    account_repository = AccountRepository()
    statement_generator = StatementGenerator()
    interest_policy = SalaryInterestPolicy()

    if bank.deposit(account, 1000):
        account_repository.save(account)

    if bank.withdraw(account, 500):
        account_repository.save(account)

    print(statement_generator.generate(account))
    print(
        "Interest earned: Rs. "
        + str(interest_policy.calculate(account.get_balance()))
    )


if __name__ == "__main__":
    main(NotificationService())
