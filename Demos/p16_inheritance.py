class MyBase:
    pass
    
class MyClass(MyBase): # Inheritance
    def __init__(self, i):
        print("It is a ctor ", i)
    def fn1(self):
        print("called - fn1")

m1 = MyClass(100)


print("debug breakpoint")
