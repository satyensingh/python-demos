employee = {"name": "suresh", "age": 27, "x":1, "y":2}

print(employee) #prints in sorted order of hash key of keys in dict.

#print(employee.name) #Error - In python dictionaries are not treated as object

print(employee["name"])

for e in employee:
    print (e, " ", hash(e))

for e in employee:
    print (e)

for key in employee:
    print (employee[key])

for key in employee["name"]:
    print (key)




