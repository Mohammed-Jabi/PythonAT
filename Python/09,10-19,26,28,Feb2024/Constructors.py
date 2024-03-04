

class Car:
    name = None
    make = None
    model = None

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start(self):
        print("Car is starting...." + self.name)
        print("Car is starting...." + self.make)
        print("Car is starting...." + self.model)

lambo = Car("Lamborghini", "2020", "Aventador")
lambo.start()

ferrari = Car("Ferrari", "2020", "F8")
ferrari.start()


