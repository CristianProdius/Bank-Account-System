class BankAccount:
    num_accounts = 0 

    def __init__(self, balance: float, account_number: int, account_holder: str):
        self.balance = balance
        self.account_number = account_number
        self.account_holder = account_holder
        BankAccount.add_account()

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    @classmethod
    def num_accounts_(cls):
        return cls.num_accounts
    
    @classmethod
    def add_account(cls):
        cls.num_accounts += 1

class SavingsAccount(BankAccount):
    def __init__(self, balance: float, account_number: int, account_holder: str, interest_rate: float, min_balance: float):
        super().__init__(balance, account_number, account_holder)
        self.interest_rate = interest_rate
        self.min_balance = min_balance

    def add_interest(self):
        if self.balance > self.min_balance:
            self.balance += self.balance * self.interest_rate / 100
        else: print("Not enouth founds")


class CheckingAccount(BankAccount):
    def __init__(self, balance: float, account_number: int, account_holder: str, overdraf_fee: float, transaction_fee: float):
        super().__init__(balance, account_number, account_holder)
        self.overdraf_fee = overdraf_fee
        self.transaction_fee = transaction_fee

    def withdraw(self, amount: float):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance = self.balance - (amount + self.overdraf_fee)

    def add_transaction(self):
        self.balance -= self.transaction_fee


def main():
    bank_account1 = BankAccount(100.96, 1, "Cristian")
    print(f"The initial balance is {bank_account1.get_balance()}")
    bank_account1.deposit(70)
    print(f"After the deposit is balance is {bank_account1.get_balance()}\n")

    bank_account2 = SavingsAccount(30.96, 1, "Cristian", 3.4, 40)
    print(f"The initial balance is {bank_account2.get_balance()}")
    bank_account2.add_interest()
    print(f"The initial balance after the intererstes have been added is {bank_account2.get_balance()}\n")

    bank_account3 = CheckingAccount(300.69, 2, "Cristian", 10, 4)
    print(f"The initial balance is {bank_account2.get_balance()}")
    bank_account3.withdraw(500)
    print(f"The balance is {bank_account2.get_balance()} after makeing the withdraw\n")

    print(f"The total accounts are {BankAccount.num_accounts_()}")


    


if __name__ == "__main__":
    main()
