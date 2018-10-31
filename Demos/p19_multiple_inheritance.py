class BankAccount:
    def __init__(self, account_holder_name, account_balance):
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

class Transactable:
    def __init__(self):
        pass
    def deposit(self, amount):
        pass

class SavingsAccount(BankAccount, Transactable):
    interest_rate = 0.4 
    def __init__(self, account_holder_name, account_balance, is_salary):
        BankAccount.__init__(self, account_holder_name, account_balance)
        self.is_salary = is_salary 
        
    def fn1(self):
        print("called - fn1")
      

m1 = SavingsAccount("Satyen", 10000, True)


print("debug breakpoint")
