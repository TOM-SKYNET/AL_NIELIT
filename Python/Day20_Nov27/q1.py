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
dt1 = 'S20,S10,S30,S15,S25'
ar = np.loadtxt("emp.csv", delimiter=",", skiprows=1, dtype=dtypee)
print(ar)
