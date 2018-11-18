import xml.dom.minidom
from os import walk,listdir

def traverseNode(document, depth=0):
  tag = document.tagName
  for child in document.childNodes:
    if child.nodeType == child.TEXT_NODE:
        print (depth*'    ', child.data)
    if child.nodeType == xml.dom.Node.ELEMENT_NODE:
      traverseNode(child, depth+1)

dir = "XML_SAMPLE_FILEs"

for filename in listdir(dir):
    print( "----------------------------" , filename , "---------------------------------------")
    dom = xml.dom.minidom.parse(dir + "/" + filename)
    traverseNode(dom.documentElement)
