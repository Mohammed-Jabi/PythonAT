#Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
#Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
class Shape:
    def area(self):
        print("Area of shape is not defined")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shape1 = Rectangle(10, 20)
print(shape1.area())
shape2 = Circle(10)
print(shape2.area())