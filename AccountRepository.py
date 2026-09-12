from abc import ABC, abstractmethod


class AccountRepository(ABC):

    @abstractmethod
    def save(self, account):
        pass

    @abstractmethod
    def load(self, account_number):
        pass
