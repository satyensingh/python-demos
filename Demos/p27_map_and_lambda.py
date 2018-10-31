def fn(x):
    return x+2

list = [1, 2, 3, 4, 5]

def mymap(func, list):
    new_list = []
    for v in list:
        z = fn(v)
        new_list += [z]
    return new_list

new_list = mymap(fn, list)
print(new_list)

# using inbuilt "map" function
new_list = map(fn, list)
print(new_list)

#let's create a lambda instead of a function "fn"
addf = lambda x : x+2

new_list = map(addf, list)
print(new_list)


#let's put lambda in func parameter
new_list = map(lambda x : x+2 , list)
print(new_list)



