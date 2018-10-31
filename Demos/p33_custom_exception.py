class SquareError: # Must inherit class BaseException in python 3.x
    def __init__(self, message):
        self.message = message

def square(x):
    if x <= 1:
        raise SquareError("number must be 2 or greater than 2")
    return x*x

try:
    ans = square(10)
    print(ans)

    ans = square(1) # Trying to generate error
    print(ans)
except SquareError as error:
    print(error.message)
except:
    print ("Some other error!")

print("done")
