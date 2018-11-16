
import xml.dom.minidom as dom
import pandas as pd

doc = dom.Document()
e1 = doc.createElement('employee')


data = pd.read_csv("emp.csv")
data = data.as_matrix()
for i in range(0,4):
    #print data[i][0], ':', data[i][1] , ':', data[i][2], ':', data[i][3]
    e11 = doc.createElement('eno')
    t11 = doc.createTextNode(str(data[i][0]))
    e11.appendChild(t11)
    e1.appendChild(e11)
    
    e12 = doc.createElement('ename')
    t12 = doc.createTextNode(str(data[i][1]))
    e12.appendChild(t12)
    e1.appendChild(e12)

    e13 = doc.createElement('edesig')
    t13 = doc.createTextNode(str(data[i][2]))
    e13.appendChild(t13)
    e1.appendChild(e13)

    e14 = doc.createElement('esalary')
    t14 = doc.createTextNode(str(data[i][3]))
    e14.appendChild(t14)
    e1.appendChild(e14)

for e in e1.childNodes:
    for t in e.childNodes:
        print t.parentNode.nodeName , t.nodeValue
        
fd = open("test.xml","w")
e1.writexml(fd, indent="\t" , newl ="\n", addindent="\t")
fd.close()

    

    
