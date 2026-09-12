# BankAccount SRP Refactor

The refactor leaves four responsibility-focused classes: `BankAccount`, `AccountRepository`, `NotificationService`, and `StatementGenerator`. `Main` is the composition point that coordinates them, rather than another domain class. Each unit can be tested with focused inputs without triggering database, email, or console-statement side effects from account operations. Changes to persistence, notification delivery, or formatting are therefore isolated from deposit and withdrawal rules.

## Section 2 — Open/Closed Principle

For the Salary Account requirement, the only existing file opened and edited was `Main.py`. The brand-new files were `Bank.py`, `SalaryAccount.py`, and `SalaryInterestPolicy.py`; `InterestPolicy.py`, `SavingsInterestPolicy.py`, and `CurrentInterestPolicy.py` did not need edits. Zero existing policy classes changed.

## Section 3 — Liskov Substitution Principle

The Square/Rectangle example breaks LSP because code using a Rectangle reasonably assumes that setting width and height are independent operations. Square violates that substitution rule by changing both dimensions from either setter, so a Square stored as a Rectangle produces 400 instead of the expected 200.

Making FixedDepositAccount implement Withdrawable and throw an exception is the wrong fix even though it compiles, because callers use Withdrawable under the substitution rule that every implementation must honor the withdrawal contract. A Fixed Deposit cannot honestly fulfill that contract, so it must not be substitutable for Withdrawable. SavingsAccount and CurrentAccount alone implement Withdrawable, and the withdrawal loop iterates over that narrower capability. No class in the final code overrides a method just to report an unsupported operation.

## Section 4 — Interface Segregation and Dependency Inversion

Across the four labs, the design moved from one class with many reasons to change toward small capability and policy contracts. If GreenLeaf adds a `WhatsAppNotificationService`, I would create `WhatsAppNotificationService.py` and touch only `Main.py` to pass that implementation into `Bank`. `Bank.py` would remain unchanged because it depends on the `NotificationService` interface, and the repository classes would also remain untouched. In the original Lab 1 design, the same requirement would have required editing the monolithic `BankAccount.py` alongside its embedded notification code and likely its caller. The final `Bank` depends only on the `AccountRepository` and `NotificationService` interfaces, while classes implement only the capability interfaces they genuinely need.
