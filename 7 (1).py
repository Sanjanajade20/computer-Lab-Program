# If an Employee object contains following details:
# empcode, empname, Date of Joining, Salary
# Write a program to serialize and deserialize this data.

import pickle
from datetime import datetime

class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def __str__(self):
        return f"Employee Code: {self.empcode}\nName: {self.empname}\nDate of Joining: {self.date_of_joining}\nSalary: {self.salary}"

def serialize_employee(emp, filename):
    with open(filename, 'wb') as file:
        pickle.dump(emp, file) 
    print(f"Employee data serialized to {filename}")

def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        emp = pickle.load(file) 
    return emp

emp = Employee(78, "Trisha Patel", datetime(2020, 5, 20), 50000)
filename = 'employee.pkl'
serialize_employee(emp, filename)
emp_from_file = deserialize_employee(filename)

print("\nDeserialized Employee Data:")
print(emp_from_file)
