
def getDiff(word):
	diffList = []
	for i in range(len(word)-1):
		diff = abs(ord(word[i+1]) - ord(word[i]))
		# print word[i+1], "-", word[i], diff
		diffList.append(diff)
	return diffList


T = int(raw_input())
for i in range(T):
	data = raw_input().rstrip()
	normal = getDiff(data) 
	reverse = getDiff(data[::-1]) 
	if normal == reverse:
		print "Funny"
	else:
		print "Not Funny"