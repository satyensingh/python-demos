import sqlite3

connection = sqlite3.connect("Emp_Master.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE employee(empid integer, empname TEXT);")
cursor.execute("INSERT INTO employee VALUES(101, 'Satyen');")
cursor.execute("INSERT INTO employee VALUES(102, 'Deepak');")
cursor.execute("INSERT INTO employee VALUES(103, 'Vicky');")

cursor.execute("SELECT * FROM employee;")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.commit()
connection.close()

