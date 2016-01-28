arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]


def isItInAreaOfOtherHourglass(foundHourglassStartingIndex, index):
	for f in foundHourglassStartingIndex:
		if index[0] >= f[0] and index[0] <= f[0]+2 \
		and index[1] >= f[1] and index[1] <= f[1]+2:
			return True
	return False

def detectAllHourglassStartingIndexes(playground):
	hourglassStartingIndexes = []
	for i in range(len(playground)):
		for j in range(len(playground[0])):
			if playground[i][j] != 0:
				if not isItInAreaOfOtherHourglass(hourglassStartingIndexes, [i,j]):
					hourglassStartingIndexes.append([i,j])
	return hourglassStartingIndexes

def gethourglassSum(playground, hourglassStartingIndex):
	total = \
	playground[hourglassStartingIndex[0] + 0][hourglassStartingIndex[1] + 0] + \
	playground[hourglassStartingIndex[0] + 0][hourglassStartingIndex[1] + 1] + \
	playground[hourglassStartingIndex[0] + 0][hourglassStartingIndex[1] + 2] + \
	playground[hourglassStartingIndex[0] + 1][hourglassStartingIndex[1] + 1] + \
	playground[hourglassStartingIndex[0] + 2][hourglassStartingIndex[1] + 0] + \
	playground[hourglassStartingIndex[0] + 2][hourglassStartingIndex[1] + 1] + \
	playground[hourglassStartingIndex[0] + 2][hourglassStartingIndex[1] + 2] 
	return total


def main(playground):
	hourglassSumList = []
	hourglassStartingIndexes = detectAllHourglassStartingIndexes(playground)
	# print(hourglassStartingIndexes)
	for i in hourglassStartingIndexes:
		total = gethourglassSum(playground, i)
		hourglassSumList.append(total)
	print(max(hourglassSumList))


def main_mod(playground):
	hourglassSumList = []
	for i in range(4):
		for j in range(4):
			total = gethourglassSum(playground, [i,j])
			hourglassSumList.append(total)

	print(max(hourglassSumList))


main_mod(arr)