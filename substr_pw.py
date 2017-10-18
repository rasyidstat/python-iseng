# after a long time not touching python!

import re

def sss(S):
	A = re.split('\d+', S)
	out = []
	for i in range(len(A)):
		cond = 0
		for j in range(len(A)):
			if A[i][j].isupper():
				cond_ = 1
			else:
				cond_ = 0
			cond = cond + cond_
		if cond > 0:
			out_ = [len(A[i))]
		else:
			out_ = [-1]
		out = out + out_
	return(max(out))
	
sss('Abd213asdl90a')
sss('asd')
sss('aBcDeFgHiJkLm')