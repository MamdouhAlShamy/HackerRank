inputList = ["2\r",
			"4\r",
			"5\r"
			]

i = 0

def raw_input():
	global i
	i += 1
	return inputList[i-1]

N = int(raw_input())

for i in range(N):
	number = int(raw_input())
	x = "{0:b}".format(number)
	print(x)