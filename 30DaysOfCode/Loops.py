inputList = ["2\r",
			"5 3 5\r",
			"0 2 10\r",
			]

i  = 0

def raw_input():
	global i
	i += 1
	return inputList[i-1]

def series(a, b, N):
	seriesList = []
	for i in range(0, N):
		if i == 0:
			item = a + (2**(i) ) * b
		else:
			item = (2**(i) ) * b
			item += seriesList[-1] 
		seriesList.append(item)
	return  seriesList

def main():
	T = int(raw_input())
	for i in range(0, T):
		seriesInfo = raw_input().rsplit()
		a = seriesInfo[0]
		b = seriesInfo[1]
		N = seriesInfo[2]
		seriesValues = series(a, b, N)
		print ' '.join(str(x) for x in seriesValues)

if __name__ == "__main__":
	# print(series(0,2,10))
	main()
	
