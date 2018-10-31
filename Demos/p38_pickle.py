# pickles = Serialization
import pickle

employee = {"name":"Satyen", "age":28}

with open("employee.ser", "w") as file:
    pickle.dump(employee, file) # serialized


with open("employee.ser", "r") as file:
    employee = pickle.load(file)
    print(employee)
