def addSpaces(res, n):
	for i in range(n):
		res += " "
	return res

def addHashes(res, n):
	for i in range(n):
		res += "#"
	return res

def addNewline(res):
	res += "\n"
	return res

N = int(raw_input())
res = ""
for i in xrange(1, N+1):
	res = addSpaces(res, N-i)
	res = addHashes(res, i)
	res = addNewline(res)
print res