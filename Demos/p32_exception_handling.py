try:
    x = 1/0
except ZeroDivisionError:
    print("Denominator cannot be Zero")
except:
    print("fail")
finally:
    print("finally")

print("done")
