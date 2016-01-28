# T # test cases
# R, C row, col of Grid
# Grid
# r,c row, col of Pattern


def readGrid():
	dim = raw_input().rstrip().split()
	row = int(dim[0])
	grid = []
	# print row
	for r in range(row):
		grid.append(raw_input().rstrip())
	return grid

def readPattern():
	dim = raw_input().rstrip().split()
	row = int(dim[0])
	pattern = []
	for r in range(row):
		pattern.append(raw_input().rstrip())
	return pattern


def getIndexesOfExpectedStartingPattern(c, gird):
	indexesOfExpectedStaringPattern = []
	for i in range(len(grid)):
		if c in grid[i]:
			indexes = [pos for pos, char in enumerate(gird[i]) if char == c]
			for ind in indexes:
				 indexesOfExpectedStaringPattern.append([i,ind])
	return indexesOfExpectedStaringPattern

def isPatternMatch(startingIndex, pattern, grid):
	patternR = len(pattern)
	patternC = len(pattern[0])
	
	for i in xrange(patternR):
		for j in xrange(patternC):
			if pattern[i][j] != grid[startingIndex[0]+i][startingIndex[1]+j]:
				return False
	return True

def removeOutOfRangeIndexes(indexesOfExpectedStaringPattern, patternDim, gridDim):
	# print indexesOfExpectedStaringPattern
	indexesToBeDeleted = []

	for i in xrange(len(indexesOfExpectedStaringPattern)):
		if indexesOfExpectedStaringPattern[i][0] + patternDim[0] > gridDim[0] \
		or indexesOfExpectedStaringPattern[i][1] + patternDim[1] > gridDim[1]:
			indexesToBeDeleted.append(i)
	
	for i in range(len(indexesToBeDeleted)-1, -1, -1):
		del indexesOfExpectedStaringPattern[indexesToBeDeleted[i]]

	# print indexesOfExpectedStaringPattern
	return indexesOfExpectedStaringPattern

def searchPatternInGrid(pattern, grid):
	indexesOfExpectedStaringPattern = getIndexesOfExpectedStartingPattern(pattern[0][0], grid)
	patternDim = [len(pattern), len(pattern[0])]
	gridDim = [len(grid), len(grid[0])]
	indexesOfExpectedStaringPattern = removeOutOfRangeIndexes(indexesOfExpectedStaringPattern, patternDim, gridDim)
	for startingIndex in indexesOfExpectedStaringPattern:
		if isPatternMatch(startingIndex, pattern, grid):
			print "YES"
			return 0
	print "NO"

T = int(raw_input())
for i in range(T):
	grid = readGrid()
	# print "grid: ", grid
	pattern  = readPattern()
	# print "pattern: ", pattern
	searchPatternInGrid(pattern, grid)
