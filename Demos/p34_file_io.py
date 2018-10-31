
f = open("sample", "w") 

# r -> open a file in read mode
# a -> open a file in append mode
# w -> Creates or open a file in write mode
# x -> strictly creates a new file else exception if file exist

f.write("hello")
f.close()


# Opens a file and closes it automatically once the job is done
with open("xyz.txt", "w") as f:
    f.write("Hola!")


with open("xyz.txt", "r") as f:
    data = f.read()
    print(data)

