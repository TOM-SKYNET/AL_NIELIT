"""
    Class operator overloading . __add__ method
"""


class vect:
    def __init__(self,px,py):
        self.x = px
        self.y = py
    def disp(self):
        print '(%.2f %.2f)'%(self.x,self.y)

    def __add__(self, v1):
        return vect(self.x+v1.x,self.y+v1.y)


v1 = vect(10.5,5.6)
v2 = vect(5.9,2.9)

v1.disp()
v2.disp()

v3 = v1 + v2
v3.disp()
