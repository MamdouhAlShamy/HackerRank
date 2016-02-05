def readData():
	inp = []
	T = int(raw_input())
	for i in range(T):
		inp.append(raw_input().rstrip())
	return inp

inp = readData()
# print inp

for word in inp:
	previousLetter = ""
	count =-1
	for currentLetter in word:
		if currentLetter == "A" and previousLetter == "B":
			pass
		elif currentLetter == "B" and previousLetter == "A":
			pass
		else:
			count += 1
		previousLetter = currentLetter
	print count