import re

def IsInteger(s):
    pat  = re.compile('.*[0-9].*')
    model = re.match(pat,s)
    if model:
        return True
    return False

def IsFloat(s):
    pat  = re.compile('.*(?=\d).*')
    model = re.match(pat,s)
    if model:
        return True
    return False

def HasVowel(s):
    pat  = re.compile('.*(?=[aeiouAEIOU]).*')
    model = re.match(pat,s)
    if model:
        return True
    return False

def IsHex(s):
    pat = re.compile(r'(\n--)([0-9A-F]+)(--)?', re.I | re.S | re.M)
    model = re.match(pat,s)
    if model:
        return True
    return False


def IsDate(s):
    pat  = re.compile('(\d{2}-\d{2}-\d{4})')
    model = re.match(pat,s)
    if model:
        return True
    return False

def IsValidPAssword(s):
    pat = re.compile('(?=.*[A-Z].*[A-Z].*)(?=.*[a-z].*[a-z].*)(?=.*[0-9).*[0-9].*)\w{8,16}')
    model = re.match(pat,s)
    if model:
        return True
    return False

def IsValidEmail(s):
    pat = re.compile(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$')
    model = re.match(pat,s)
    if model:
        return True
    return False

def Normalise(s):
    return 0

def Normalisen(s,n):
    return 0
try:
    print ("IsInteger: " , IsInteger('a daa 11'))
    print ("IsFloat: ", IsFloat('dsfs 11.0 aaa'))
    print ("HasVowel: ", HasVowel('apple'))
    print ("isHex: ", IsHex('77094A27E'))
    print ("isDate: ", IsDate('12/02-1999'))
    print ("IsValidPAssword: ", IsValidPAssword('dd2AcD1pass.com'))
    print ("isValidEmail: ", IsValidEmail('hhsdasdadasasdas.com'))

except Exception as e:
    print (e)


