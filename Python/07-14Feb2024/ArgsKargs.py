def arg(*args):
    for arg in args:
        print(arg, end= " ")

arg(1)
arg(1,2)
arg(1,2,3)
arg(1,2,3,4)
arg(1,2,3,4,5)


def make_pizza(size, *toppings):
    #sprint("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping, end = " ")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



