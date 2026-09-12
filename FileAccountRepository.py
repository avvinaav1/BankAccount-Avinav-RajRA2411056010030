import os

from AccountRepository import AccountRepository
from BankAccount import BankAccount


class FileAccountRepository(AccountRepository):

    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, account):
        records = []

        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                records = file.read().splitlines()

        new_record = (
            f"{account.get_account_number()},"
            f"{account.get_name()},"
            f"{account.get_balance()}"
        )
        account_number = str(account.get_account_number())
        replaced = False
        updated_records = []

        for record in records:
            if record.split(",", 1)[0] == account_number:
                updated_records.append(new_record)
                replaced = True
            else:
                updated_records.append(record)

        if not replaced:
            updated_records.append(new_record)

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(updated_records) + "\n")

    def load(self, account_number):
        if not os.path.exists(self.file_path):
            return None

        with open(self.file_path, "r", encoding="utf-8") as file:
            for record in file.read().splitlines():
                fields = record.split(",", 2)
                if len(fields) == 3 and fields[0] == str(account_number):
                    return BankAccount(
                        int(fields[0]),
                        fields[1],
                        float(fields[2]),
                    )

        return None
