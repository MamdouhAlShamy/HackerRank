	
def getNumberOf5And3(N):
	if N % 3 == 0:
		numberOfFive = N
		numberOfThree = 0
		return [numberOfFive, numberOfThree]
	elif N % 5 == 0:
		numberOfFive = 0
		numberOfThree = N
		return [numberOfFive, numberOfThree]
	else:
		# ls = []
		for i in xrange(1, (N/2) +1):
			j = N - i
			# print i,j
			if i % 3 == 0 and j % 5 == 0:
				if i > j:
					return i,j
					# ls.append([i, j])
			elif i % 5 == 0 and j % 3 == 0:
				if j > i:
					# ls.append([j, i])
					return j,i
	# 	if len(ls) == 0:
	# 		ls.append("-1")
	# return ls
	return -1



T = int(raw_input())
for i in xrange(T):
	N = int(raw_input())
	res = getNumberOf5And3(N)
	print res
	# print "DONE"
	# if res == -1:
	# 	print res
	# else:
	# 	val = ""
	# 	for i in xrange(res[0]):
	# 		val += "5"
	# 	for i in xrange(res[1]):
	# 		val += "3"
	# 	print val