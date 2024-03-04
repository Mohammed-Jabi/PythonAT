class A:
    def method(self):
        return "Method A"

class B(A):
    def method(self):
        return "Method B"

class C(A):
    def method(self):
        return "Method C"

class D(B,C):
    def method(self):
        return "Method D"


