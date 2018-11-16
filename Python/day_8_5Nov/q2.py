
class Employee:
    def __init__(self,name,empno,basicpay):
        self.name = name
        self.empno = empno
        self.basicpay = basicpay
    def display(self):
        print "Name =%s , EmpNo = %d, Basis Pay=%f"%(self.name,self.empno,self.basicpay)
        
class Scientist(Employee):
    def __init__(self,name,empno,basicpay,ta,category):
        Employee.__init__(self,name,empno,basicpay)
        #super(Scientist,self).__init__(name,empno,basicpay)
        self.ta = ta
        self.category = category
    def display(self):
        #Employee.display()
        Employee.display()
        #super(Scientist,self).display()
        print "Technical allowance=%d, Category = %s"%(self.ta,self.category)
    def __str__(self):
        return "Scientist {} with id {} has a salary of {}".format(self.name,self.empno,self.basicpay)
    
class Officer(Employee):
    def __init__(self,name,empno,basicpay,grade,department):
        Employee.__init__(self,name,empno,basicpay)
        #super(Officer,self).__init__(name,empno,basicpay)
        self.grade = grade
        self.department = department
    def display(self):
        Employee.display()
        #super(Officer,self).display()
        print "Grade=%d, Department = %s"%(self.grade,self.department)
    def __str__(self):
        return "Officer {} with id {} has a salary of {}".format(self.name,self.empno,self.basicpay)

name = raw_input("Name")
empno = input("Employee No")
pay = input("Employee Basic Pay")
ta = input("Technical allowance")
category = raw_input("Category")
           
s = Scientist(name,empno,pay,ta,category)
s.display()
s = str(s)

grade = raw_input("Grade")
dept = raw_input("department")
o = Officer(name,empno,pay,grade,dept)
o.display()

#s1 = str(s) + '\n and' + str(o)
#print s1
