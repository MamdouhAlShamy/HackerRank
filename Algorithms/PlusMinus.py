def readData():
	N = int(raw_input())
	array = raw_input().rstrip().split()
	array = map(int, array)
	return array


def function(array):
	N = float(len(array))
	countOfNegativeNumbers = 0
	countOfZeros = 0
	countOfPositiveNumbers = 0
	for n in array:
		if n < 0 :
			countOfNegativeNumbers += 1
		elif n == 0:
			countOfZeros += 1
		elif n > 0:
			countOfPositiveNumbers += 1
		else:
			print "So weird" 
	print countOfPositiveNumbers/N
	print countOfNegativeNumbers/N
	print countOfZeros/N



array = readData()
function(array)