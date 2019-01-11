
"""
    Multiplication Table in a single line from user input. Write to a file from command line
"""

import sys

open(sys.argv[1],'w').writelines(['%d X %s = %d \n'%(x,sys.argv[2],int(sys.argv[2]) * x) for x in range(1,11) ])