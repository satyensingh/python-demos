#refer mymodule.py for class description

from modules import mymodule
#import modules.mymodule

mymodule.fn()

m1 = mymodule.MyClass()

m1.fn1()

print(mymodule.MyClass.__doc__) # Reading the description about the class
print (mymodule.MyClass.fn1.__doc__) # Reading the description about the function


# Try below from python CLI:-

# > from modules import mymodule
# > help mymodule.MyClass
