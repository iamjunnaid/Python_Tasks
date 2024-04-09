'''
Encapsulation: Name Mangling to access private members

'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


Emma = Employee('Emma', 5000)
print('Name of Employee: ',Emma.name)

#Name Mangling to Access the Private Member (Attribute)
print('Salary of the Employee is: ',Emma._Employee__salary)