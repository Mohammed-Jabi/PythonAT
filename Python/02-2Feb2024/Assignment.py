number = input('Enter a number: ')
for i in range(11):
    print(number, '  x ', i, ' = ', int(number) * i)


# In the above code, we are taking input from the user and then using a for loop to print the multiplication table of the given number.

num1, num2 = input('Enter two numbers: ').split()
print('Sum:', int(num1) + int(num2))