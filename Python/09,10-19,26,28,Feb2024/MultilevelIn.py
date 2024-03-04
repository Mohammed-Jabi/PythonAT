class GF:
    def home(self):
        print("Home")

class F(GF):
    pass

class S(F):
    pass

s = S()
s.home()
f = F()
f.home()
