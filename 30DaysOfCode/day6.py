# N = raw_input()


def printSpace(string, n):
	for i in range(0,n):
		string += " "
	return string

def printHash(string, n):
	for i in range(0,n):
		string += "#"
	return string

def drawStairs(N):
	string = ""
	for i in range(0, N):
		string = printSpace(string, N-i-1)
		string = printHash(string, i+1)
		string += "\n"
	print(string)
			

drawStairs(6)
