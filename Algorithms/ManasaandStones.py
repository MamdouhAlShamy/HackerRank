T = int(raw_input())
for i in xrange(T):
	n = int(raw_input())
	a = int(raw_input())
	b = int(raw_input())
	possibleLastStones = []
	for i in range(0, n):
		lastStone = (n -1 -i) * a + i * b
		if lastStone not in possibleLastStones:
			possibleLastStones.append(lastStone)
	possibleLastStones.sort()
	print " ".join(str(stone) for stone in possibleLastStones)