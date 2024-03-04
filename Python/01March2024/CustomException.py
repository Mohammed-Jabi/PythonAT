class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter amount to withdraw: "))
if withdraw > balance:
    raise MyCustomException("Insufficient balance")
else:
    print("Withdraw successful", balance)