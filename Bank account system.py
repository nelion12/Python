# Creating a simple bank account system in Python involves defining classes for accounts and methods for common operations like depositing, withdrawing, and checking balances. Below is an example implementation:

# Bank Account System Implementation
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    # Creating a bank account instance
    account = BankAccount("John Doe", 1000.0)

    # Checking balance
    account.check_balance()  # Output: Account holder: John Doe, Balance: $1000.00

    # Depositing money
    account.deposit(500)     # Output: Deposited $500.00. New balance: $1500.00

    # Withdrawing money
    account.withdraw(200)    # Output: Withdrew $200.00. New balance: $1300.00

    # Attempting to withdraw more than the balance
    account.withdraw(2000)   # Output: Insufficient balance.

    # Checking balance again
    account.check_balance()   # Output: Account holder: John Doe, Balance: $1300.00


#Explanation
#BankAccount Class:

#The __init__ method initializes the account holder's name and the initial balance (default is 0.0).
#The deposit method allows depositing money into the account.
#The withdraw method allows withdrawing money, checking for sufficient balance first.
##Example Usage:

#An instance of BankAccount is created for "John Doe" with an initial balance of $1000.00.
#he program demonstrates checking the balance, depositing money, and withdrawing money, including handling insufficient funds.
#Enhancements
#This basic implementation can be expanded with additional features, such as:

#Interest calculations.
#Multiple account types (e.g., savings, checking).
#Account number generation.
#Transaction history tracking.
#Feel free to modify or expand upon this code based on your requirements! If you have any specific features in mind or need further assistance, let me know!


class BankAccount:
    def init(self, balance):
        self.__balance = balance  # Protected attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive")
    def get_balance(self):
        return self.__balance
Account = BankAccount()
print(Account.get_balance())


