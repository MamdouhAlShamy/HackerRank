
def readMatrix():
	N = int(raw_input())
	matrix = []
	for i in xrange(N):
		r = raw_input().rstrip()
		row = []
		for j in r:
			row.append(int(j))
		matrix.append(row)
	return matrix

# def isCavity(matrix, index):


def getIndex(matrix):
	N = len(matrix)
	index = []
	for i in range(1, N-1):
		for j in range(1, N-1):
			index.append([i,j])
	return index
			
def checkCavity(index):
	for ind in index:
		center = matrix[ind[0]][ind[1]]
		right = matrix[ind[0]][ind[1]+1]
		left = matrix[ind[0]][ind[1]-1]
		up = matrix[ind[0]-1][ind[1]]
		down = matrix[ind[0]+1][ind[1]]
		if center > right and center > left and center > up and center > down:
			matrix[ind[0]][ind[1]] = "X"

def writeMatrix():
	for i in range(len(matrix)):
		row = ""
		for j in range(len(matrix)):
			row += str(matrix[i][j])
		print row

matrix = readMatrix()
index = getIndex(matrix)
checkCavity(index)
writeMatrix()