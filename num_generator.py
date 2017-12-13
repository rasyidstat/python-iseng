import random

# xyyy
# x = 9, y = 10


# param
num = list(range(0,10))
num_first = list(range(1,10))
num_pos = []

# generate number
print("generating the possible number")
for a in num_first:
	for b in num:
		for c in num:
			for d in num:
				fill = int(str(a)+str(b)+str(c)+str(d))
				num_pos = num_pos + [fill]

# get a single digit
print("get a single digit")
def num_single(x):
	y = ''
	x = str(x)
	for i in range(len(x) - 1):
		y = y + str(int(x[i]) + int(x[i+1]))[-1]
	return(y)

def num_recursive(x):
	x = str(x)
	while len(x) != 1:
		x = num_single(x)
	return(x)

# get final number
num_output = list(map(lambda x: num_recursive(x), num_pos))
print(num_output)

# get summary
# c = dict()
# for i in num_output:
# 	c[i] = c.get(i, 0) + 1
# print(c)


