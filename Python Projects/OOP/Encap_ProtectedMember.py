'''
Protected Member
Protected members are accessible within the class and also available to its sub-classes. To define a protected member, 
prefix the member name with a single underscore _.

'''

class Company:
    def __init__(self):
        self._project = 'NLP'

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 
        Company.__init__(self)

    def show(self):
        print('Employee Name: ',self.name,' and it\'s Salary is: ',self.salary)
        print('Project: ',self._project)

katri = Employee('Katri',5000)
katri.show()