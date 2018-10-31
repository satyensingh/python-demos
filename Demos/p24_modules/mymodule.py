def fn():
    print("fn")

class MyClass:
    def fn1(self):
        print ("myclass - fn1")

# When importing a module anything written outside the function/class will get executed as soon as module is imported
# To avoid executing these code write these code under below if condition in all module file
if __name__ == "__main__": 
    print("I am not a module")
else:
    print("I am a module, loaded successfully...")

