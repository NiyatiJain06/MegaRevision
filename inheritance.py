# parent class

class Vehicle:
    def start(self):
        print("Vehicle is starting")

# child class.
 
class car(Vehicle):
    def drive(self):
        print("Car is now moving!")

class bike(Vehicle):
    def ride(self):
        print("Bike is now riding!")

class truck(Vehicle):
    def load(self):
        print("Truck is loading goods!")        

c = car()
c.start()
c.drive()

b = bike()
b.start()
b.ride()

t = truck()
t.start()
t.load()
        