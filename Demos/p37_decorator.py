#Security Module
def security_decorator(secure_function):
    def wrapper():
        print("Applying Security")
        secure_function()
        print("Successful")
    return wrapper



#Critical Functions
@security_decorator # add_employee = security_decorator(add_employee)
def add_employee():
    print("employee added")


@security_decorator # delete_employee = security_decorator(delete_employee)
def delete_employee():
    print("employee deleted")


#Calling Secure Functions
add_employee()
delete_employee()

