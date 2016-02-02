

def isSpring(number):
	return number % 2 == 0

T = int(raw_input())
for i in xrange(T):
	size = 1
	N = int(raw_input())
	if N != 0:
		for i in xrange(1, N+1):
			if isSpring(i):
				size += 1
			else: # Summer
				size *= 2
	print size
