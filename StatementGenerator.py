class StatementGenerator:

    def generate(self, account):
        lines = [
            (
                f"---- Statement for Account "
                f"#{account.get_account_number()} "
                f"({account.get_name()}) ----"
            ),
            *account.get_transaction_log(),
            f"Current Balance: Rs. {account.get_balance()}",
            "-----------------------------------------------------",
        ]

        return "\n".join(lines)
