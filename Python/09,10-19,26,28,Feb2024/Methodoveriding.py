#Methodoveriding is a feature that allows a subclass to provide a specific implementation of a method that is already provided by one of its super-classes.
class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def __init__(self):
        pass
    def sound(self):
        super().sound()
        print("Dog Sound")

animal = Animal()
animal.sound()
dog = Dog()
dog.sound()