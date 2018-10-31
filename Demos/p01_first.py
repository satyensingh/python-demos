import sys

print (sys.getrefcount(1))

x = 1

print (sys.getrefcount(x))

