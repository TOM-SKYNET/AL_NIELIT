
class vect:
    def __init__(self,px,py):
        self.x = px
        self.y = py
    def disp(self):
        print '(%d %d)'%(self.x,self.y)

    def __add__(self, v1):
        return vect(self.x+v1.x,self.y+v1.y)

    def __equ__(self,v1):
        if self.x == v1.x and self.y == v1.y :
            return True
        else:
            return False
        
v1 = vect(10,5)
v2 = vect(10,5)

v1.disp()
v2.disp()

v3 = v1 + v2
v3.disp()

print 'v1 == v2 ::', v1==v2

