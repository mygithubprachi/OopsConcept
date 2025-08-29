from abc import ABC, abstractmethod
from datetime import datetime

# ------------------------------
# Abstraction (Abstract Base Class)
# ------------------------------
class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance   # Encapsulation (private attribute)
        self.created_at = datetime.now()

    # Abstract method (must be implemented in subclasses)
    @abstractmethod
    def account_type(self):
        pass

    # Encapsulation: using getter & setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# ------------------------------
# Inheritance
# ------------------------------
class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"


class CurrentAccount(Account):
    def account_type(self):
        return "Current Account"


# ------------------------------
# Polymorphism
# ------------------------------
def print_account_details(account: Account):
    print(f"Account Type: {account.account_type()}")
    print(f"Owner: {account.owner}")
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.get_balance()}")
    print(f"Created On: {account.created_at}")
    print("-" * 40)


# ------------------------------
# Driver Code
# ------------------------------
if __name__ == "__main__":
    acc1 = SavingsAccount(1001, "Prachi", 5000)
    acc2 = CurrentAccount(1002, "Rahul", 10000)

    acc1.deposit(2000)
    acc1.withdraw(1000)

    acc2.withdraw(500)
    acc2.deposit(2500)

    # Polymorphism in action
    print_account_details(acc1)
    print_account_details(acc2)
