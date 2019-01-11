"""
    Display only number containing text using regular expression from a text file

"""

import re

f = open("f1.txt")
lines = f.readlines()
for line in lines:
    mo = re.match('.*[0-9]+.*',line)
    if mo:
        print line

