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

#This is for testing purpose
#This is for testing purpose
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)