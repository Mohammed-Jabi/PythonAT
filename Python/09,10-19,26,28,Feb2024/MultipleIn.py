class father:
    def father(self):
        print("Father")

    def home(self):
        print("Father-Home")

class mother:
    def mother(self):
        print("Mother")

    def home(self):
        print("Mother-Home")

class son(father, mother):
    pass

son = son()
print(son.father())
print(son.mother())
print(son.home())
#MRO - Method Resolution Order