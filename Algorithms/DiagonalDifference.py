

def readMatrix():
	N = int(raw_input())
	matrix = []
	for i in xrange(N):
		matrix.append(map(int, raw_input().rstrip().split()))
	return matrix

def getSlashDiagonalSum(matrix):
	N = len(matrix)
	total = 0
	for i in xrange(N):
		total += matrix[i][i] 
	return total

def getBackSlashDiagonalSum(matrix):
	N = len(matrix)
	total = 0
	for i in xrange(N):
		total += matrix[i][N-1-i] 
	return total


def getDifferenceBetweenSumsOfMatrixDiagonals(matrix):
	slashDiagonalSum = getSlashDiagonalSum(matrix)
	backSlashDiagonalSum = getBackSlashDiagonalSum(matrix)
	return abs(slashDiagonalSum - backSlashDiagonalSum)

matrix = readMatrix() 
res = getDifferenceBetweenSumsOfMatrixDiagonals(matrix)
print res