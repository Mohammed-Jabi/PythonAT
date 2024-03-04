#Encapsulation
#Encapsulation is the mechanism that binds together code and the data it manipulates, and keeps both safe from outside interference and misuse.
#Data encapsulation led to the important OOP concept of data hiding.

class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = "10"

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Not Authorized")

    def set_password(self, password):
        if len(password) > 6:
            self.__password = password
        else:
            print("Password should be more than 6 characters")

password = Password("123456")
password.get_password(True)
password.set_password("123")

