

s = raw_input("Enter a Sentence")

p = s.split()
o = 0
for v in p:
	if v in v[::-1]:
		o+=1
		
if o>1 :
	print 'no of palidarome', o


