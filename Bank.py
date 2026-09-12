from AccountRepository import AccountRepository
from NotificationService import NotificationService


class Bank:

    def __init__(
        self,
        notification_service: NotificationService,
        account_repository: AccountRepository,
    ):
        self.notification_service = notification_service
        self.account_repository = account_repository

    def deposit(self, account, amount):
        if not account.deposit(amount):
            return False

        self.account_repository.save(account)
        self.notification_service.send(
            "Deposit completed for account "
            + str(account.get_account_number())
        )
        return True

    def withdraw(self, account, amount):
        if not account.withdraw(amount):
            return False

        self.account_repository.save(account)
        self.notification_service.send(
            "Withdrawal completed for account "
            + str(account.get_account_number())
        )
        return True
