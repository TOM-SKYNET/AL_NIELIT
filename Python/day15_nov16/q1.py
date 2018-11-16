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
    pat  = re.compile(r'.*(?=[\u]).*')
    model = re.match(pat,s)
    if model:
        return True
    return False

def IsDate(d):
    pat  = re.compile(r'.*(?=[\u]).*')
    model = re.match(pat,s)
    if model:
        return True
    return False

print "IsInteger: ", IsInteger('a daa 11')
print "IsFloat: ", IsFloat('dsfs 11.0 aaa')
print "HasVowel: ", HasVowel('apple')
print "isHex: ", IsHex('hh\\x12')



