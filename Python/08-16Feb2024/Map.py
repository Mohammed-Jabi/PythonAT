#Map
import math
def squaere(number):
    return number ** 2

l1 = [1,2,3,4,5,6,7,8,9,10]
#map takes a function and a list as an argument and applies the function to all the elements of the list
power = list(map(squaere,l1))
print(power)

def squareroot(number):
    return math.sqrt(number)

l2 = [1,2,3,4,5,6,7,8,9,10]
sqrt = list(map(squareroot,l2))
print (sqrt)
