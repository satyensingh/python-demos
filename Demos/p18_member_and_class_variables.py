class BankAccount:
    def __init__(self, account_holder_name, account_balance):
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

class SavingsAccount(BankAccount):
    interest_rate = 0.4 # All variables initialized/used without self are class member
    def __init__(self, account_holder_name, account_balance, is_salary):
        BankAccount.__init__(self, account_holder_name, account_balance)
        self.is_salary = is_salary # initialised/used using self makes it instance member
        
    def fn1(self):
        print("called - fn1")
      

m1 = SavingsAccount("Satyen", 10000, True)

print (m1.account_balance)
print (m1.account_holder_name)
print (m1.is_salary)

print (SavingsAccount.interest_rate)
print (m1.interest_rate) # If instance does not have a member it is pulled from class

m1.interest_rate = 10.2
print (SavingsAccount.interest_rate)
print (m1.interest_rate)
print (SavingsAccount.interest_rate)

SavingsAccount.interest_rate = 20.4
print (SavingsAccount.interest_rate)
print (m1.interest_rate)
print (SavingsAccount.interest_rate)

#Instances can update the values of class member using "__class__"
m1.__class__.interest_rate = 50.55 # same as SavingsAccount.interest_rate = 50.55
print (SavingsAccount.interest_rate)
print (m1.interest_rate)
print (SavingsAccount.interest_rate)


print("debug breakpoint")
