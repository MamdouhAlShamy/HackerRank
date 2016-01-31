import math

def getStringSpaceFree(sentence):
	sentence = sentence.split()
	sentence = ''.join(w for w in sentence)
	return sentence

def getGridDimentions(sentence):
	L = len(sentence)
	# print L
	sq = math.sqrt(L)
	# print sq
	numberOfColumns = int(math.ceil(sq))
	numberOfRows = int(math.floor(sq))
	# print numberOfRows, numberOfColumns
	if numberOfRows * numberOfColumns >= L:
		return numberOfRows,numberOfColumns
	else:
		return numberOfColumns, numberOfColumns

def getGrid(dim, sentence):
	grid = []
	for i in range(0, dim[0]):
		start =  i * dim[1]
		end = start +  dim[1]
		grid.append(sentence[start:end])
	return grid

def encrypt(dim, grid):
	sentence = ""
	for j in range(dim[1]):
		for i in range(dim[0]):
			try:
				sentence += grid[i][j]
			except:
				pass
		sentence += " "
	return sentence



# sentence = "if man was meant to stay on the ground god would have given us roots"
# sentenceSpaceFree = getStringSpaceFree(sentence)
# sentenceSpaceFree = "chillout"

sentenceSpaceFree = raw_input().strip()
dim = getGridDimentions(sentenceSpaceFree)
grid = getGrid(dim, sentenceSpaceFree)
print encrypt(dim, grid)