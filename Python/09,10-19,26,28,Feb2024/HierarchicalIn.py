class Vehica:
    def info(self):
        print("This is a vehicle")

class Car(Vehica):
    def info(self):
        print("This is a car")

class Bike(Vehica):
    def info(self):
        print("This is a bike")

c = Car()
c.info()
b = Bike()
b.info()
v = Vehica()
v.info()