'''
Method Overriding
We have a vehicle class as a parent and a 'Car' and 'Truck' as its sub-class. But each vehicle can have a different 
seating capacity, speed, etc., so we can have the same instance method name in each class but with a different implementation. 
Using this code can be extended and easily maintained over time.

'''


class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    
    def show(self):
        print('Details are:',self.name,self.color,self.price)

    def speed(self):
        print('The max speed is 150 kmph')

    def motor(self):
        print('It has 7 gears')

class Car(Vehicle):
    def speed(self):
        print('Car speed is 300 kmph')
    def motor(self):
        print('It has 5 gears')

car = Car('Porsche', 'Red',200000)
car.show()
car.speed()
car.motor()


Truck = Vehicle('Volvo', 'Silver',80000)
Truck.show()
Truck.speed()
Truck.motor()