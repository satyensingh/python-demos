import mymodule

mymodule.fn()

print("using_mymodule",__name__)

# __name__ is a property of module that is implicitly created by python.
# It is same as IIFE in JavaScript.
# everything written in .js goes in IIFE likewise...
# everyhing written in .py goes in a module named same as the value of __name__
# but the moment we import the file the value of the property __name__ changes to a file name that it is written in.
#python appln has only one "__main__" as a value of property __name__
