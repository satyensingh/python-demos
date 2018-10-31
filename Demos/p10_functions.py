def fn1():
    def fn2():
        print ("fn2")
    print ("fn1")
    fn2()

    #def fn3():
    #    print ("fn3")
    #return fn3 # Return func To call it from outside the parent function

    def fn4():
        print("fn4")
        return "r-fn4"
    return fn4() #call and return what fn4 is returning

fn1()
#fn2() # Error - can't call nested func from outside the parent function

f3 = fn1()
#f3()

returnedFn4 = fn1()
print returnedFn4

#Debugging from terminal
#--> python -m pdb p10_function