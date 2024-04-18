'''
Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a 
default value of 50.

'''

class Vehicle:
    def __init__(self,name, max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The bus {self.name} has maximum speed {self.max_speed} with people capacity of {capacity}"
    
    #Method overriding

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
volvo = Bus('Volvo',180,12)
print(volvo.seating_capacity())