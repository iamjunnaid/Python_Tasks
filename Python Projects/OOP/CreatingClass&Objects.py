'''
Creating Class and Object in Python

'''

class Employee:
    #class varaible
    company = "Prisma"

    #constructor to initialize the object
    def __init__(self,name,salary,location):
        # Instance Variable
        self.name = name
        self.salary = salary
        self.location = location
    
    #Instance Method
    def show(self):
        print('The Employee details are: ',self.name,self.salary,self.location, self.company)

# Creating Objects
employee1 = Employee('Alex', 2799, "Oulu")
employee1.show()

employee2 = Employee('Kari', 2150, "Turku")
employee2.show()

employee3 = Employee('Jonas', 3599, "Tampere")
employee3.show()

