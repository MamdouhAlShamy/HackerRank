
T = int(raw_input())
for i in range(T):
	N = raw_input()
	count = 0
	for n in N:
		if int(n) == 0:
			pass
		elif int(N) % int(n) == 0:
			count += 1
	print count
