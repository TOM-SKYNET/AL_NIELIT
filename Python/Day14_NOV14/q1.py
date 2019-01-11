"""
	Regular Expression findall. Write to a file , all scientist using regular expression
"""

import re

fd = open("emp.csv")
lines  = fd.readlines()
f = open("sci.csv","w+")
for line in lines:
	if len(re.findall('scientist',line)) > 0:
		f.writelines(line)
	
fd.close()
f.close()
