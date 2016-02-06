T = int(raw_input())
for i in range(T):
	NCM = raw_input().rstrip().split()

	N = int(NCM[0])
	C = int(NCM[1])
	M = int(NCM[2])

	numberWrappers = N/C
	eatenChocolates = numberWrappers
	while  numberWrappers / M > 0  :
		rewardedChocolates = int(numberWrappers / M)
		numberWrappers -= (rewardedChocolates *M)
		# print "numberWrappers: ", numberWrappers
		# print "rewardedChocolates: ", rewardedChocolates
		eatenChocolates += rewardedChocolates 
		numberWrappers += rewardedChocolates
	print eatenChocolates



