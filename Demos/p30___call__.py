class Adder:
    def add(self, x, y):
        return x+y
    def __call__(self, a, b):
        return self.add(a, b)

adder = Adder()
#sum = adder.add(10, 20) # __call__ not required
sum = adder(10, 20) # must have __call__ func def and implicitly calls it with the parameter passed.
print (sum)

