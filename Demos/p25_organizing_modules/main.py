#If the modules are in a folder than we cannot import the module unless we create a file "__init__.py" under that folder.
#And while importing we must use "from" keyword with foldername that contain __init__.py file followed by import keyword

#we can also import without "from" - refer line number 8.


#from modules import mymodule
import modules.mymodule

modules.mymodule.fn()

m1 = modules.mymodule.MyClass()

m1.fn1()

print(modules)
print(modules.mymodule)

print(modules.mymodule.MyClass.__module__)


