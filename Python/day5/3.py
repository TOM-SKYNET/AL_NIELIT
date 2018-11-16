
def letcount(s):
	ccd=dict()
	for ch in s:
		if ch in ccd:
			ccd[ch] +=1
		else:
			ccd[ch]=1
	return ccd


s = raw_input("Enter a word")

print letcount(s)



