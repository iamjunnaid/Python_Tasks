'''
Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is 
seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

'''

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount = amount + (amount * 10/100)
        return amount


volvo = Bus("School Volvo", 20, 50)
print("Total Bus fare is:", volvo.fare())

#Check type of the "volvo" object
print(type(volvo))


# Check if "volvo" is also an instance of the Vehicle class
print(isinstance(volvo,Vehicle))