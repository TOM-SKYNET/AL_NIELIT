
"""
Create a module that contains functions for performing the following(use re).
 (Slno 1 to 6 should return boolean )
 1.IsInteger-Should take one parameter as string and should contain integer for True else False.
 2.IsFloat-Should take one parameter as string and if it contains a float return True else False.
 3.HasVowel-supplied string should contain at least one vowel char for True else False.
 4.IsHex - supplied string should contain only hex digits,if so True else False.
 5.IsDate - True if given a date in DD-MM-YYYY format.
 6.IsValidPassword - True is the given string containas - 8 to 16 alphanumerics,at least 2 digits,at least 2 lowercase letters
			and atleast two uppercase letters
 7.IsValidEmail-True if the given string is valid email id.


 8.Normalise -  to replace all instances of one or more whitespace characters with a single space.
 9.Normalisen-  to replace all instances of one or more whitespace characters with  n spaces.
		this function should take two parameters- string and n, make n def parameter with value 1.

 10.Test the module.


"""

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
    return re.sub('\s+', ' ', s)

def Normalisen(s,n=1):
    return re.sub(r'(\s)\1{n,}', r'\1', s)

try:
    print ("IsInteger: " , IsInteger('a daa 11'))
    print ("IsFloat: ", IsFloat('dsfs 11.0 aaa'))
    print ("HasVowel: ", HasVowel('apple'))
    print ("isHex: ", IsHex('77094A27E'))
    print ("isDate: ", IsDate('12/02-1999'))
    print ("IsValidPAssword: ", IsValidPAssword('dd2AcD1pass.com'))
    print ("isValidEmail: ", IsValidEmail('hhsdasdadasasdas.com'))
    print ("Normalise: ", Normalise('hhsd     asd  ada    sas das.   com'))
    print ("Normalisen: ", Normalisen('hhsd     asd    ada    sas das \t .   com'))
    print ("Normalisen: ", Normalisen('hhsd     asd    ada    sas das \t .   com', n=2))

except Exception as e:
    print (e)


