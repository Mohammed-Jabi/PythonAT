#Class & Object in Python

class Person:

    #Attributes -> Data members
    name = None
    age = None
    city = None
    email = None

    #Methods -> Member functions
    def talk(self):
        print("TAlking....")

    def walk(self):
        print("Walking....")

#Object
person1 = Person()
person1.name = "J"
print(person1.name)
