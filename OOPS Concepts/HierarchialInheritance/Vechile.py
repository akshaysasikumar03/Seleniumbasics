class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Bike(Vehicle):
    def ride(self):
        print("Bike Ride")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
bike1 = Bike()
bike1.start()
bike1.ride()
car1 = Car()
car1.drive()
car1.start()
