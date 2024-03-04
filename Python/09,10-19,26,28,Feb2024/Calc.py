class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        print(a - b)

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calc = Calc()
calc.sub(10, 20)
calc = calc.add(10, 20)
print(calc)