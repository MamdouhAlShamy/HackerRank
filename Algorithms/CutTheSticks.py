N = int(raw_input())
sticks = raw_input().rstrip().split()
sticks = map(int, sticks)

while len(sticks) != 0:
	sticksCut = 0
	cutSize = min(sticks)
	for i in range(len(sticks)-1, -1, -1):
		if sticks[i] <= cutSize:
			del sticks[i]
		else:
			sticks[i] -= cutSize 
		sticksCut += 1
	print sticksCut	
