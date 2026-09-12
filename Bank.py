class Bank:

    def __init__(self, notification_service):
        self.notification_service = notification_service

    def deposit(self, account, amount):
        if not account.deposit(amount):
            return False

        self.notification_service.send(
            "Deposit completed for account "
            + str(account.get_account_number())
        )
        return True

    def withdraw(self, account, amount):
        if not account.withdraw(amount):
            return False

        self.notification_service.send(
            "Withdrawal completed for account "
            + str(account.get_account_number())
        )
        return True
