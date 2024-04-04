'''
We can delete the object property by using the del keyword. After deleting it, if we try to access it, we will get an error.

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
        print('The Employee name is',self.name,',it\'s salary is ', self.salary, 'located at ', self.location, 'and works in ', self.company)
        
# Creating Objects
employee1 = Employee('Alex', 2799, "Oulu")
employee1.show()

employee2 = Employee('Kari', 2150, "Turku")
employee2.show()

employee3 = Employee('Jonas', 3599, "Tampere")
employee3.show()

#Deleting the Object property and then confirming it by showing the Error
del employee1.name
print(employee1.name)

