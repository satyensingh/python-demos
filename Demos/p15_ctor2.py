# In python, function overloading is not supported and hence ctor overloading is not.

class MyClass:
    def __init__(self):
        print("It is a ctor")
    def __init__(self, i):
        print("It is a ctor ", i)
    def fn1(self):
        print("called - fn1")

#m1 = MyClass() # Error
m1 = MyClass(100) # calls the ctor


print("debug breakpoint")