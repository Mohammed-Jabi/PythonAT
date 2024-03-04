side1 = print(int(input("Enter the length of the first side: ")))
side2 = print(int(input("Enter the length of the second side: ")))
side3 = print(int(input("Enter the length of the third side: ")))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")