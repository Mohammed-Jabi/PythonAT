#Abstraction
#Abstraction is the concept of hiding the real implementation of an application from the user and emphasizing only the usage of it. In other words, the user will have the information on what the object does instead of how it does it. Abstraction is the process of hiding the implementation details and showing only the functionality to the user. Abstraction can be achieved with either abstract classes or interfaces

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
       pass


class Dog(Animal):
    def sound(self):
        print("Dog Sound")

dog = Dog("Dog")
dog.sound()