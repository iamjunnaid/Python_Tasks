'''
Create Class Method Using @classmethod Decorator

'''

from datetime import date

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #Class Method decrotor
    @classmethod
    def cal_age(cls,name,birth_year):
        return cls(name,date.today().year-birth_year)
    
    def show(self):
        print(self.name,"'s age is: ",self.age)

jess = Student('Jessica',20)
jess.show()

alex = Student.cal_age("Alex",1990)
alex.show()
