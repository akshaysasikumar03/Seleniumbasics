class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self):
        print("Car is speeding")
class Musicsystem:
    def music(self):
        print("Musicsystem is running")
class Smartcar(Car, Musicsystem):
    def autopilot(self):
        print("Autopilot is running")
smartcar1 = Smartcar()
smartcar1.start()
smartcar1.drive()
smartcar1.music()
smartcar1.autopilot()