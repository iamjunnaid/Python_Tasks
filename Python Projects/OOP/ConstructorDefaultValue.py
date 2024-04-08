'''
Constructor With Default Values
Python allows us to define a constructor with default values. The default value will be used if we do not pass arguments 
to the constructor at the time of object creation.

'''

class Students:

    def __init__(self, name, age =12, classroom = 7):
        self.name = name
        self.age = age
        self.classroom = classroom

    def show(self):
        print(self.name, 'is',self.age,'year old and studing in class',self.classroom)

emma = Students('Emma')
emma.show()

ali = Students('Ali',13)
ali.show()

katri = Students('Katri',14,8)
katri.show()

