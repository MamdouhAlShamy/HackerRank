NT = raw_input().rstrip().split()
N = int(NT[0])
T = int(NT[1])

width = raw_input().rstrip().split()
width = map(int, width)

for i in range(T):
	enterAndExitLane = raw_input().rstrip().split()
	enterLane = int(enterAndExitLane[0])
	exitLane = int(enterAndExitLane[1])
	print min(width[enterLane:exitLane+1])
