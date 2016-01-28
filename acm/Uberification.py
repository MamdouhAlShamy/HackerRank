# 2	>> number of Test Cases

# 5 5	>> N M : N nodes M edges

# 1 2 >> node# node#
# 2 3
# 3 1
# 2 4
# 1 5

# 4 3

# 1 2
# 2 3
# 2 4

class Pair:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.ways = []

	def addWay(self, way):
		self.ways.append(way)

	def getNumberOfWays(self):
		return len(self.ways)


def constructGraph(numberOfNodes, edges):
	graph = {}
	for n in range(1, numberOfNodes+1):
		graph[n] = []

	for edge in edges:
		graph[edge[0]].append(edge[1])
		graph[edge[1]].append(edge[0])

	print("graph: ")
	print(graph)
	return graph

def getProblem1(graph):

	ways = []

	ways12 = Ways(1,2)
	ways12.addWay([1,2])
	ways12.addWay([1,3,2])
	ways.append(ways12)

	ways13 = Ways(1,3)
	ways13.addWay([1,2,3])
	ways13.addWay([1,3])
	ways.append(ways13)

	ways14 = Ways(1,4)
	ways14.addWay([1,2,4])
	ways14.addWay([1,3,2,4])
	ways.append(ways14)

	ways15 = Ways(1,5)
	ways15.addWay([1,5])
	ways.append((ways15))

	ways23 = Ways(2,3)
	ways23.addWay([2,1,3])
	ways23.addWay([2,3])
	ways.append(ways23)

	ways24 = Ways(2,4)
	ways24.addWay([2,4])
	ways.append(ways24)

	ways25 = Ways(2,5)
	ways25.addWay([2,1,5])
	ways25.addWay([2,3,1,5])
	ways.append(ways25)

	ways34 = Ways(3,4)
	ways34.addWay([3,1,2,4])
	ways34.addWay([3,2,4])
	ways.append(ways34)

	ways35 = Ways(3,5)
	ways35.addWay([3,1,5])
	ways35.addWay([3,2,1,5])
	ways.append(ways35)

	ways45 = Ways(4,5)
	ways45.addWay([4,2,1,5])
	ways45.addWay([4,2,3,1,5])
	ways.append(ways45)

	return ways

# path = []
# possibleWays = []
# parent = []
# def getPossibleWays(start, end, graph):
# 	global path, parent
# 	global possibleWays
# 	for point in graph[start]:
# 		path.append(start)
# 		parent.append(start)
# 		if point in path:
# 			# dead end path
# 			path.remove(point)
# 		elif point == end:
# 			#path found
# 			path.append(point)
# 			print("path: ")
# 			print(path)
# 			possibleWays.append(path)
# 			print("possibleWays: ")
# 			print(possibleWays)
# 		else:
# 			# path.append(point)
# 			return getPossibleWays(point, end, graph)

def getPath(point, end, graph, parentList):
	print("parentList: " + str(parentList))
	if point in parentList:
		# loop detected
		return []
	elif point == end:
		# path found
		tmp = parentList
		tmp.append(point)
		return tmp
	else:
		parentList.append(point)
		for newPoint in graph[point]:
			getPath(newPoint, end, graph, parentList)

def getPossibleWays(start, end, graph):
	paths = []
	# parentList = [start]
	for point in graph[start]:
		path = getPath(point, end, graph, [start])
		if not path:
			pass
		else:
			print("path: " + str(path))
			paths.append(path)
	return paths

def constructPaths(graph, numberOfNodes):
	# return getProblem1(graph)
	system = []
	global possibleWays
	for i in range(1, numberOfNodes+1):
		for j in range(i+1, numberOfNodes+1):
			print("pair(" + str(i) + ", " + str(j) + ")")
			possibleWays = getPossibleWays(i,j, graph)
			print(possibleWays)
			pair = Pair(i,j)
			for path in possibleWays:
				pair.addWay(path)
			system.append(pair)
	return system



def main():
	numberOfUniqueWays = 0
	graph = constructGraph()
	print(graph)
	system = constructPaths(graph)
	for pair in system:
		if pair.getNumberOfWays() == 1 : 
			numberOfUniqueWays += 1

	print("no of unique ways: " + str(numberOfUniqueWays))


# 1 2 >> node# node#
# 2 3
# 3 1
# 2 4
# 1 5

noOfNodes = 5
edges = [ [1,2], [2,3], [3,1], [2,4], [1,5] ]
graph = constructGraph(noOfNodes, edges)
x = constructPaths(graph, noOfNodes)
print(x)