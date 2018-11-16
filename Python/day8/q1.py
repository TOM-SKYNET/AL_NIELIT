
class employee:
    empno=100

    def store(self,name, sal):
        employee.empno= employee.empno+1
        self.name = name
        self.salary = sal

    def display(self):
        print 'Emp # %d , Name: %s, Salary %f'%(employee.empno,self.name,self.salary)

e = employee()
e.store('Tom', 2000)
e.display()
