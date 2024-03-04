class Father:

    def threeBHK(self):
        print("Father has 3BHK")

    def car(self):
        print("Father has a car")

class Son(Father):

        pass

s = Son()
s.threeBHK()
s.car()