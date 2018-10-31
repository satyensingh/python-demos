import dis

def fn():
    i = 1
    if i < 10:
        print("yes")
    else:
        print("no")

fn()
print ("x")

dis.dis(fn) #disassembling the function only

#run it from terminal with "python -m dis p07_.py"