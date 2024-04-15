'''
Multiple Inheritance
In multiple inheritance, one child class can inherit from multiple parent classes. So here is one child class and 
multiple parent classes.

'''

class Person:
    def person_information(self,name,age):
        self.name = name
        self.age = age
        print(name,'is',age,'years old')

class Company:
    def company_information(self,title,location,field):
        self.title = title
        self.location = location
        self.field = field
        print(title,'is located at',location,'and works in',field,'domain')

class Employee(Person,Company):
    def employee_information(self,skill,salary):
        self.skill = skill
        self.salary = salary
        print('Salary:',salary,'and proficient in',skill,)

em = Employee()

em.person_information('Junnaid',21)
em.company_information('Google','Austin','Software')
em.employee_information('Python',135000)