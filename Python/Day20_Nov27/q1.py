'''
1 Create a numpy structured array using the emp.csv file available in common folder.
1.1 display all the records.
1.2 display names of officers.
1.3 display all the scientists records.
1.4 display the total salary.
1.5 display average salary of engineers.
1.6 display employees in the ascending order of salary.
1.7 display employees in the ascending order of designation and then salary.
1.8 display the lowest salary for scientist designation.
1.9 display records of employees who are scientists and are drawing the lowest salary(without using sort).
'''

import numpy as np
dtypee = np.dtype([('ename','S20'),('eno','i4'),('edesig','S25'),('esalary','f8'),('ephno','S20')])

# Q1.1 display all the records.
ar = np.loadtxt("emp.csv", delimiter=",", skiprows=1, dtype=dtypee)
print(ar)

# 1.2 display names of officers
emp = np.rec.array(ar)
print "-----------names of officers-------------------"
print ar[ar['edesig'] == 'officer']

# 1.3 display all the scientists records.
print "-------------all the scientists records---------------"
print ar[ar['edesig'] == 'scientist']

# 1.4 display the total salary
print "----------------------------"
print 'Total Salary :', ar['esalary'].sum()

# 1.5 display average salary of engineers
print "----------------------------"
print 'Average salary of engineers :', ar[ar['edesig'] == 'engineer']['esalary'].mean()

#1.6 display employees in the ascending order of salary.
print "-------------- Employees in the ascending order of salary --------------"
ar1 = ar.copy()
ar1.sort(order='esalary')
print ar1

# 1.7 display employees in the ascending order of designation and then salary
print "------------Employees in the ascending order of designation and then salary---------------"
ar2 = ar.copy()
ar2.sort(order=['edesig','esalary'])
print ar2

# 1.8 display the lowest salary for scientist designation
print "--------------- Lowest salary for scientist designation -----------------"
print ar[ar['edesig'] == 'scientist']['esalary'].min()

# 1.9 display records of employees who are scientists and are drawing the lowest salary(without using sort).
print "---------- Employees who are scientists and are drawing the lowest salary(without using sort) -------------"
ar3 = ar[ar['edesig'] == 'scientist']
print ar3[ar3['esalary'] == ar3['esalary'].min() ]