#Factorial

number = int(input('Enter a number: '))
if number < 0:
    print('Invalid input')
elif number == 0:
    print('Factorial is 1')
else:
    fact = 1
    for i in range(1, number + 1):
        fact *= i #fact = fact * i
print('Factorial of', number, 'is', fact)