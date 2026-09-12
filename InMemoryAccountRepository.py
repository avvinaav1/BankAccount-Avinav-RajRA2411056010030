from AccountRepository import AccountRepository


class InMemoryAccountRepository(AccountRepository):

    def __init__(self):
        self.accounts = {}

    def save(self, account):
        self.accounts[account.get_account_number()] = account

    def load(self, account_number):
        return self.accounts.get(account_number)
