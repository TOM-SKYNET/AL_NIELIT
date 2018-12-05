"""
    # Q1 Using the emp.csv file avilable in the common folder, create a data frame object named ef1
"""

import pandas as pd
import numpy as np

ef1 = pd.read_csv("../Day20_Nov27/emp.csv")
print ef1
ef0 = ef1.copy()

ef1['eno'][2] = np.nan
ef1['eno'][4] = np.nan
ef1['eno'][6] = np.nan
#print ef1

# Q2 Remoe all non-digit charaters from empno column and store the new data in ef2
ef2 = ef1.fillna(0)
print (ef2)

# Q3 Write the three coulmns ename, edesig and esalary to the excel file empx.xlsx with sheet name as salary
wo = pd.ExcelWriter('empx.xlsx')
ef3 = pd.DataFrame(ef1[['ename','edesig','esalary']])
ef3.to_excel(wo, sheet_name='Salary', index=False)
wo.save()

# Q4 Write the two columns ename and ephno to the same execl file empx.xlsx with sheet name as phone
ef4 = ef1[['ename','ephno']]
ef4.to_excel(wo, sheet_name='Phone', index=False)
wo.save()
wo.close()

# Q5 In the data frame ef2 make edesig and eno as row_index & store the new data in ef3
ef3 = ef0.set_index(['edesig','eno'])
print ef3

# Q6 in ef3 , sort the index edesig and store in ef4
ef4 = ef3.sort_values(['edesig'])
print ef4

# Q 6.1 Using ef4, display all scientist records
ef4 = ef4.reset_index()
print ef4.loc[ef4['edesig'] == 'scientist',:]

# Q 6.2 Display average salary of engineers
print 'Average Salary :', ef4.loc[ef4['edesig'] == 'engineer','esalary'].sum() / ef4.loc[ef4['edesig'] == 'engineer','esalary'].count()

# Q 6.3 Display the lowest salary for scientist designation
print 'Lowest Salary :', ef4.loc[ef4['edesig'] == 'scientist','esalary'].min()