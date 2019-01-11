"""
    Function for printing class hierarchy. BaseException, Exception
"""

def pch(cn, noh=0):
    print '-' * noh, cn.__name__
    for n in cn.__subclasses__():
        pch(n, noh+2)

pch(Exception)

    
