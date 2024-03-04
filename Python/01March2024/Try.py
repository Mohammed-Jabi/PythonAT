class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            c = a / b
        except Exception as e:
            print("Enter integr only")
        else:
            print("a/b = ", c)
        finally:
            print("Finally block is always executed")

x = XYZ()
x.f1()