age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

x= int(input("Enter a number: "))
y= int(input("Enter another number: "))

if x>y:
    print(x, "is greater than", y)
elif x==y:
    print(y, "is greater than", x)
elif x<y:
    print(y, "is greater than", x)
else:
    print("Invalid input")

numbers1 = int(input("Enter a number: "))
numbers2 = int(input("Enter another number: "))
numbers3 = int(input("Enter another number: "))

maxnum = max(numbers1, numbers2, numbers3)
print("The maximum number is: ", maxnum)