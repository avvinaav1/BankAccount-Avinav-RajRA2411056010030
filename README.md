# BankAccount SRP Refactor

The refactor leaves four responsibility-focused classes: `BankAccount`, `AccountRepository`, `NotificationService`, and `StatementGenerator`. `Main` is the composition point that coordinates them, rather than another domain class. Each unit can be tested with focused inputs without triggering database, email, or console-statement side effects from account operations. Changes to persistence, notification delivery, or formatting are therefore isolated from deposit and withdrawal rules.

## Section 2 — Open/Closed Principle

For the Salary Account requirement, the only existing file opened and edited was `Main.py`. The brand-new files were `Bank.py`, `SalaryAccount.py`, and `SalaryInterestPolicy.py`; `InterestPolicy.py`, `SavingsInterestPolicy.py`, and `CurrentInterestPolicy.py` did not need edits. Zero existing policy classes changed.
