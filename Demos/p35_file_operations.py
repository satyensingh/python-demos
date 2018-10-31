with open("xyz.txt", "r") as f:
    data = f.read() # Reading complete file
    print(data)


print("**********************************************************")

with open("xyz.txt", "r") as f:
    data = f.readline() 
    print(data)


print("**********************************************************")

with open("xyz.txt", "r") as f:
    for x in f:
        print(x)


print("**********************************************************")

with open("xyz.txt", "r") as f:
    for x in f:
        x = x.rstrip("\n") # stripping from right side of line
        print(x)


print("**********************************************************")

with open("xyz.txt", "r") as f:
    data = f.readlines() # Reading complete file into a list of lines
    print(data)


print("**********************************************************")

with open("xyz.txt", "r") as f:
    data = f.readlines()
    new_data = map(lambda x : x.rstrip("\n"), data)
    print(new_data)


print("**********************************************************")

with open("persons", "r") as f:
    for x in f:
        new_data = map(lambda x : x.rstrip("\n"), x)
        print(new_data)
        
