#Class  -Students,Cources, Pyment,
#Student -> person1, person2, person3
#Course -> course1, course2, course3

class Students:
    name = None
    age = None
    city = None
    email = None

    def watchrecordings(self):
        print("Watchrecordings....")

    def doassignment(self):
        print("Do assignments....")

    def docoding(self):
        print("Do coding....")

student1 = Students()
student2 = Students()
student3 = Students()

class Courses:
    name = None
    duration = None
    fee = None
    type = None

    def watchrecordings(self):
        print("Watchrecordings....")

    def doassignment(self):
        print("Do assignments....")

    def docoding(self):
        print("Do coding....")

course1 = Courses()
course2 = Courses()
course3 = Courses()

class Payment:
    amount = None
    date = None
    mode = None
    status = None

    def pay(self):
        print("Pay....")

    def refund(self):
        print("Refund....")

    def cancel(self):
        print("Cancel....")

payment1 = Payment()
payment2 = Payment()
payment3 = Payment()