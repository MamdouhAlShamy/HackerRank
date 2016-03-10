
def readInput():
	stones = []
	N = int(raw_input())
	for i in range(N):
		stones.append(raw_input().strip())
	return stones

def removeDuplicated(stones):
	stonesArray = []
	for stone in stones:
		stonesArray.append("".join(set(stone)))
	return stonesArray


stones = readInput()
uniqueStones = removeDuplicated(stones)
count = 0
foundGemElement = True

for element in max(uniqueStones):
	for stone in uniqueStones:
		if element not in stone:
			foundGemElement = False
			break
	if foundGemElement:
		count += 1
	foundGemElement = True
print count
