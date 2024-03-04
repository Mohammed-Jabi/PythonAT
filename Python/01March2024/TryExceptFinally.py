try:
    number1 = int(input("Enter a number: "))
    number2 = input("Enter a number: ")
    number3 = number1 / number2
except ValueError as v:
    print("Error: ", v)
except ZeroDivisionError as z:
    print("Error: ", z)
except TypeError as t:
    print("Error: ", t)
except Exception as e:
    print("Error: ", e)
else:
    print("number1/number2 = ", number3)
finally:
    print("Finally block is always executed")
