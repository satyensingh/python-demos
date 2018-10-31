# Diamond Problem has been solved by going breadth instead of depth search in inheritance level
# Other Diamond Problem is solved automatically as python is explicit

class SuperClass:
    diamond = "heera"

class BankAccount(SuperClass):
    #diamond = "BankAccount ka heera"
    pass
    
class Transactable(SuperClass):
    #diamond = "Transactable ka heera"
    pass

class SavingsAccount(BankAccount, Transactable):
    #diamond = "SavingsAccount ka heera"      
    pass

m1 = SavingsAccount()

print (m1.diamond)


print("debug breakpoint")
