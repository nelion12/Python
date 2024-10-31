class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ksh{amount:.2f}. New balance: ksh{self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ksh{amount:.2f}. Remaining balance: ksh{self.balance:.2f}"
        else:
            return "Withdrawal amount exceeds balance."

    def get_balance(self):
        return f"Account balance: ksh{self.balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ksh{interest:.2f} applied. New balance: ksh{self.balance:.2f}"


class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ksh{amount:.2f}. Remaining balance: ksh{self.balance:.2f}"
        else:
            return "Withdrawal amount exceeds balance and overdraft limit."


# Example usage
if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings = SavingsAccount("123456", "Alice", 1000)
    checking = CheckingAccount("789012", "Bob", 500)

    # Deposit and withdraw from SavingsAccount
    print(savings.deposit(200))          # Deposited ksh200. New balance: ksh1200.00
    print(savings.apply_interest())      # Interest of ksh24.00 applied. New balance: ksh1224.00
    print(savings.withdraw(300))         # Withdrew ksh300. Remaining balance: ksh924.00

    # Deposit and withdraw from CheckingAccount
    print(checking.deposit(100))         # Deposited ksh100. New balance: ksh600.00
    print(checking.withdraw(650))        # Withdrew ksh650. Remaining balance: ksh-50.00
    print(checking.get_balance())        # Account balance: ksh-50.00


