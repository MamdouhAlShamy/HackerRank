
inp = []
def readInput():
	T = long(raw_input())
	for i in range(T):
		inp.append(long(raw_input().rstrip()))
readInput()

# inp = [12L,5L,7L,1L]
# inp=[2L]


import math

def isPrime(n):
	if n % 2 == 0:
		return False
	else:
		i = 3
		while i < math.sqrt(n):
			# print i
			if n % i == 0:
				return False
			i += 2
		return True

for i in inp:
	if i<0:
		print "Not prime"
	elif i == 2:
		print "Prime"
	elif i == 1 or i == 0:
		print "Not prime"
	elif isPrime(i):
		print "Prime"
	else:
		print "Not prime"
