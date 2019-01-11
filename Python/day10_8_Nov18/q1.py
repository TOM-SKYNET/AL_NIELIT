""" Abstarct Classes Employee , Engineer, Officer, JEngineer, SEngineer"""

import abc

class Employee:
    __metaclass__ = abc.ABCMeta
    def __init__(self,pname,pno,pbay):
        self.name = pname
        self.no = pno
        self.basic = pbay
        self.da = .3 * self.basic
        self.hra = .1 * self.basic
        self.spa = 0  
        
    @abc.abstractmethod
    def calcSpa(self):
        pass
    @abc.abstractmethod
    def calcHra(self):
        pass
    def calcSal(self):
        self.salary = self.basic + self.da + self.hra + self.spa
    def disp(self):
        self.calcHra()
        self.calcSal()
        print "Name :%s, EmpNo:%d, Net Salary:%f"%(self.name,self.no,self.salary)
        
class Engineer(Employee):
    def calcSpa(self):
        self.spa  = .2 * self.basic

class Officer(Employee):
    def calcSpa(self):
        self.spa  = .1 * self.basic
    def calcHra(self):
        self.hra = .1 * self.basic
        
class JEngineer(Engineer):
    def calcHra(self):
        self.hra = self.hra + 500
            
class SEngineer(Engineer):
    def calcHra(self):
        self.hra = self.hra + 1000

sEng = SEngineer('Varun', 101, 70000)
jEng = JEngineer('Chinnu', 102, 55000)
off = Officer('Vimala', 102, 99000)
sEng.disp()
jEng.disp()
off.disp()
