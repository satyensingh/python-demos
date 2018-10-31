def fn():
    print("fn")

class MyClass:
    '''This is the description of MyClass''' # class Documentation
    def fn1(self):
        '''This is the description of function "fn" ''' # funct documentation
        print ("myclass - fn1")


if __name__ == "__main__": 
    print("I am not a module")
else:
    print("I am a module, loaded successfully...")

