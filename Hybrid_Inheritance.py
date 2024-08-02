#HYBRID_INHERITANCE
#******************
class emp():
    def nasa(self):
        self.name = input("ENTER YOUR NAME:")
        self.sal = float(input("ENTER YOUR SALARY:"))

class adds(emp):
    def pros(self):
        self.hra = E.sal*5/100
        self.da = E.sal*4/100
        self.ta = E.sal*3/100
        self.add = self.hra + self.da + self.ta 
        print("YOUR HRA, DA, TA amount is",self.add)

class subs(emp):
    def cons(self):
        self.pf = E.sal*3/100
        self.lic = E.sal*2/100
        self.loan = E.sal*2/100
        self.sub = self.pf + self.lic + self.loan
        print("YOUR PF, LIC, LOAN amount is",self.sub)

class equ(adds,subs):
    def gross(self):
        self.gross_sal = E.sal + A.add - S.sub
        print("HELLO!",E.name,",YOUR GROSS SALARY IS",self.gross_sal)

E = emp()
E.nasa()
A = adds()
A.pros()
S = subs()
S.cons()
F = equ()
F.gross()