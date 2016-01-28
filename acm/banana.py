# Enter your code here. Read input from STDIN. Print output to STDOUT

inputList = [4,
			"I = mo\r",
			"love = amo\r",
			"icecream = gelatooo\r",
			"banana = banana\r",
			2,
			3,
			"I love banana\r",
			3,
			"I love icecream\r"
			]

i  = 0

def raw_input():
	global i
	i += 1
	return inputList[i-1]


def makeWordDictionary():
	N = int(raw_input())
	wordDictionary = {}
	for i in range(0,N):
	    word = raw_input()
	    word = word.split(" = ")
	    wordDictionary[word[0]] = (word[1]).rsplit()[0]
	return wordDictionary

def translateSentence():
	global wordDictionary
	K = int(raw_input())
	EnglishSentence = raw_input()
	words = EnglishSentence.rsplit()
	# print(words)
	MinioneseSentenceList = []
	for i in range(0,K):
		# print(wordDictionary[words[i]])
		MinioneseSentenceList.append(wordDictionary[words[i]])
	print(" ".join(MinioneseSentenceList))

def handleSentences():
	T = int(raw_input())
	for i in range(0,T):
		translateSentence()

def main():
	global wordDictionary
	wordDictionary = makeWordDictionary()
	# print(wordDictionary)
	handleSentences()



if __name__ == "__main__":
	# for i in range(0, len(inputList)):
	# 	x = raw_input()
	# 	print(str(x))
	main()