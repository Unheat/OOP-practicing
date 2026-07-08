class BankAccount:
    def __init__(self, owner_name: str, account_number: str, balance: float):
        # TODO: initialize self._owner_name, self._account_number, and self._balance
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: float) -> bool:
        # TODO: add amount to balance if amount > 0, return True if succes
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        # TODO: subtract amount from balance if balance >= amount, return True
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def display_account(self):
        # TODO: print "owner_name (account_number) | Balance: $balance"
        # Hint: use f"${self._balance:.2f}" for formatting
        print(f"{self._owner_name} ({self._account_number}) | Balance: $" + str(self._balance))


class SavingsAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str,
                 balance: float, interest_rate: float):
        super().__init__(owner_name, account_number, balance)
        # TODO: initialize self._interest_rate
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> bool:
        # TODO: only allow if (balance - amount) >= 100
        if self._balance - amount >= 100:
            self._balance -= amount
            return True
        return False

    def apply_interest(self):
        # TODO: add (balance * interest_rate / 100) to balance
        self._balance += self._balance * self.interest_rate / 100
        pass


class CheckingAccount(BankAccount):
    def __init__(self, owner_name: str, account_number: str,
                 balance: float, overdraft_limit: float):
        super().__init__(owner_name, account_number, balance)
        # TODO: initialize self._overdraft_limit
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        # TODO: allow if (balance + overdraft_limit) >= amount
        if self._balance + self.overdraft_limit >= amount:
            self._balance += amount
            return True
        return False


if __name__ == "__main__":
    savings = SavingsAccount("Alice", "SAV-001", 1000, 2.0)
    savings.display_account()
    print(f"Withdraw $950: {str(savings.withdraw(950)).lower()}")
    savings.apply_interest()
    savings.display_account()

    print()

    checking = CheckingAccount("Bob", "CHK-002", 500, 300)
    checking.display_account()
    print(f"Withdraw $700: {str(checking.withdraw(700)).lower()}")
    checking.display_account()