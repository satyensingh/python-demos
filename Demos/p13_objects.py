#creating class
class MyClass:
    def fn1(self): # Here, "self" is like a "this". It is a keyword and passed explicitly.
        print("called - fn1")

#creating instance
m1 = MyClass()

print(m1)

m1.fn1() # "m1" goes as "self"

#The above call is Same as below
MyClass.fn1(m1)

print(type(m1))

print("debug breakpoint")