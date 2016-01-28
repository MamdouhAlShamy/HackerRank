def divisorSum(n):
	ls = [1,n]
	for i in range(2, n):
		if n%i == 0:
			ls.append(i)
	return ls


print divisorSum(12)
