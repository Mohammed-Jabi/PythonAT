#Match Case
#Match case is a new feature in Python 3.10. It is used to compare the values of the variable with the given pattern. If the value of the variable matches with the pattern, then the block of code is executed. If the value of the variable does not match with the pattern, then the block of code is not executed.

number = int(input('Enter a number: '))
match number:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
    case 4:
        print('Four')
    case 5:
        print('Five')
    case 6:
        print('Six')
    case 7:
        print('Seven')
    case 8:
        print('Eight')
    case 9:
        print('Nine')
    case 10:
        print('Ten')
    case _:
        print('Greater than 10 or less than 0')