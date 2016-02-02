import math

def readInputData():
	numbers = raw_input().rstrip().split()
	numbers = map(int, numbers)
	return numbers

def function(numbers):
	print int(math.floor(math.sqrt(numbers[1])) - math.ceil(math.sqrt(numbers[0]))+1)

T = int(raw_input())
for i in range(T):
	numbers = readInputData()
	function(numbers)