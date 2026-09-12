from abc import ABC, abstractmethod


class Transferable(ABC):

    @abstractmethod
    def transfer(self, target, amount):
        pass
