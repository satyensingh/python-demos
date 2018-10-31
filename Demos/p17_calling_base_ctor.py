class MyBase:
    def __init__(self):
        print("base Ctor")
    
class MyClass(MyBase):
    def __init__(self):
        MyBase.__init__(self)  # calling base ctor is explicit in python
        print("derived ctor ")
        MyBase.__init__(self) # not necessary it has to be at 1st line and can occur multiple times.
    def fn1(self):
        print("called - fn1")
        MyBase.__init__(self) # can also be called from member function

m1 = MyClass()


print("debug breakpoint")
