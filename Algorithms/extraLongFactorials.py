
N = int(raw_input())

# N = 100

def factorial(N):
	if N == 1:
		return 1
	else:
		return N * factorial(N-1)

print factorial(N)