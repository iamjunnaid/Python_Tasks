'''
Getters and Setters in Python
Use the getter method to access data members and the setter methods to modify the data members.

'''


class Student:
    def __init__(self, name, age, standard):
        self.name = name
        self.__age = age
        self.__standard = standard

    def show(self):
        print('Student Detail:', self.name, self.__age, self.__standard)

    #Getter for Age and Standard
    def get_age(self):
        return self.__age
    def get_standard(self):
        return self.__standard
    
    # Setter for Standard
    def set_standard(self,number):
        if number > 9:
            print('Invalid')
        else:
            self.__standard = number
        
jon = Student('Jon', 10, 8)
jon.show()

jon.set_standard(10)
jon.set_standard(6)
jon.show()

    

    

        