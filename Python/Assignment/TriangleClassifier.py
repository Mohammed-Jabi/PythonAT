#Triangle Classifier
#Side1 == Side2 == Side3 = Equilateral
#Side1 == Side2 or Side2 == Side3 or Side1 == Side3 = Isosceles
#Side1 != Side2 != Side3 = Scalene

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")