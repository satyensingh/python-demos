class Summation:
    def sum(self, x):
        return x+1
    
    def __call__(self, x):
        return x+2

s = Summation()

list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = map(s, list)
print(new_list)