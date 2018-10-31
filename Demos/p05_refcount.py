import sys

def func(z):
  print (sys.getrefcount(z)) #ref count is incremented by 2 as the func getrefcount also has a parameter that points to "1"

yy = 1
print (sys.getrefcount(yy))
func(yy)