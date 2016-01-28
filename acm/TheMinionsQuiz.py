class Node:
	def __init__(self, value, level):
		self.node = { "value" : value
					, "NumberOfAnding" : 0
					, "NumberOfOring" : 0
					, "level" : level
					 }

	def andingHappened(self):
		self.node["NumberOfAnding"] += 1

	def oringHappened(self):
		self.node["NumberOfOring"] += 1

	def getValue(self):
		return self.node["value"]
	
	def getNumberOfAnding(self):
		return self.node["NumberOfAnding"]

	def setNumberOfAnding(self, number):
		self.node["NumberOfAnding"] = number
	
	def getNumberOfOring(self):
		return self.node["NumberOfOring"]

	def setNumberOfOring(self, number):
		self.node["NumberOfOring"] = number

	def getLevel(self):
		return self.node["level"]

	def printNode(self):
		x = "Value: " + str(self.node["value"]) \
			+ " NumberOfAnding: " + str(self.node["NumberOfAnding"]) \
			+ " NumberOfOring: " + str(self.node["NumberOfOring"]) \
			+ " level: " + str(self.node["level"]) 
		print(x)

	def isLevel(self, level):
		return self.node["level"] == level


def makePossibleNodes(x, y, level):
	# print(str(x) + " " + str(y) + " " + str(level))
	createdList = []
	try:
   		val = int(x)
		node1 = Node((x|y), level)
		node1.oringHappened()

		node2 = Node((x&y), level)
	   	node2.andingHappened()
		createdList.append(node1)
		createdList.append(node2)
   	except:
   		node1 = Node(x.getValue() | y, level)
   		node1.setNumberOfOring(x.getNumberOfOring() + 1)
   		node1.setNumberOfAnding(x.getNumberOfAnding())

   		node2 = Node(x.getValue() & y, level)
   		node2.setNumberOfAnding(x.getNumberOfAnding() + 1)
   		node2.setNumberOfOring(x.getNumberOfOring())

		createdList.append(node1)
		createdList.append(node2)
	return createdList

def getNodesWithLevel(listOfNodes, level):
	nodesWithGivenLevelList = []
	for node in listOfNodes:
		if node.isLevel(level):
			nodesWithGivenLevelList.append(node)
	return nodesWithGivenLevelList


def getLeafLevel(listOfNodes):
	leafLevel = 0
	for node in listOfNodes:
		nodeLevel = node.getLevel()
		if  nodeLevel > leafLevel:
			leafLevel = nodeLevel
	return leafLevel



def func(numbers, A, B):
	listOfNodes = []
	# print(numbers)
	firstTime = True

	for i in range(0, len(numbers)-1):
		if firstTime:
			createdNodesList = makePossibleNodes(numbers[i], numbers[i+1], i+1)
			listOfNodes.append(createdNodesList[0])
			listOfNodes.append(createdNodesList[1])
			# print(str([node.getValue() for node in listOfNodes]))
			firstTime = False
		else:
			nodes = getNodesWithLevel(listOfNodes, i) 
			for node in nodes:
				createdNodesList = makePossibleNodes(node, numbers[i+1], i+1)
				listOfNodes.append(createdNodesList[0])
				listOfNodes.append(createdNodesList[1])

	leafLevel = getLeafLevel(listOfNodes)
	# print("leafLevel: " + str(leafLevel))

	listOfLeaves = getNodesWithLevel(listOfNodes, leafLevel)
	# print("no of leaf nodes: " + str(len(listOfLeaves)))

	result = []
	for node in listOfLeaves:
		if (node.getNumberOfAnding() == A):
			if (node.getNumberOfOring() == B):
				result.append(node)
	
	# print([node.printNode() for node in result])
	resultValue = [node.getValue() for node in result]
	maxValue = max(resultValue)
	# print("max: " + str(maxValue))
	return maxValue

T = int(raw_input())
for i in range(0, T):
	AB = raw_input()
	tmp = AB.rsplit()
	A = int(tmp[0])
   	B = int(tmp[1])
   	numbers = raw_input()
   	tmpN = numbers.rsplit()
   	g = [int(n) for n in tmpN]
   	x = func(g, A, B)
   	print(x)
