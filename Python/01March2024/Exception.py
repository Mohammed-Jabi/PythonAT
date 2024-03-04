#Exception
#Exception is an error that occurs during the execution of a program. When that error occurs, Python generate an exception that can be handled,
# which avoids your program to crash.

#Exceptions can be handled using a try and except block. The code that could potentially have an error is put in the try block.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))


try:
    c = a / b
    print("a/b = ", c)
except Exception as e:
    print("Error: ", e)

print("Hello")