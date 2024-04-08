'''
Constructor Chaining

Constructor chaining is the process of calling one constructor from another constructor. Constructor chaining is 
useful when you want to invoke multiple constructors, one after another, by initializing only one instance.

'''

class Vehicle:
    def __init__(self,engine):
        self.engine = engine

class Car(Vehicle):

    def __init__(self,engine, max_speed):
        super().__init__(engine)
        #print('Inside Car')
        self.max_speed = max_speed

class Electric(Car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inisde Elecric Car')
        self.km_range = km_range
class Petrol(Car):
    def __init__(self, engine, max_speed, fuel_tank):
        super().__init__(engine,max_speed)
        print('Inside Petrol Fuel Car')
        self.fuel_tank = fuel_tank

BYD = Electric('1500cc', 280,450)
print(f"Engine = {BYD.engine}, Max Speed = {BYD.max_speed}, KM Range = {BYD.km_range}")

TOYOTA = Petrol('1500cc', 320,'45L')
print(f"Engine = {TOYOTA.engine}, Max Speed = {TOYOTA.max_speed}, Fuel Tank = {TOYOTA.fuel_tank}")
