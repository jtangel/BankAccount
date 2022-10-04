class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient funds: this bank is nice and will not charge you')
        else: self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_instances(cls):
        for account in cls.accounts:
            account.display_account_info()

Account1 = BankAccount(0.01, 34598)
Account2 = BankAccount(0.02, 2345432)

Account1.deposit(556).deposit(495).deposit(1000).withdraw(32000).yield_interest().display_account_info() 

Account2.deposit(1000).deposit(3000).withdraw(100000).withdraw(50).withdraw(10000).withdraw(3000).yield_interest().display_account_info()


BankAccount.print_all_instances() 




