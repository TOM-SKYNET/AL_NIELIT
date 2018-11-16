
class compnos:
    def __init__(self,pa,pb):
        self.a = pa
        self.b = pb
    def disp(self):
        print 'Complex (%2f + %2fi)'%(self.a,self.b)

    def __add__(self, v1):
        return compnos(self.a+v1.a,self.b+v1.b)
    def __mul__(self, v1):
        return compnos((self.a*v1.a)-(self.b*v1.b),(self.a*v1.b)+(self.b*self.a))

v1 = compnos(10.5,5.6)
v2 = compnos(5.9,2.9)

v1.disp()
v2.disp()

v3 = v1 * v2
v3.disp()
