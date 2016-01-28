

# N = int(raw_input())
N = 3

def isOdd(N):
	if N%2 != 0 :
		return True
	else:
		return False

if isOdd(N):
	print("Weird")
else:
	if N >= 2 and N <= 5:
		print("Not Weird")
	elif N >= 6 and N <= 20:
		print("Weird") 
	elif N > 20:
		print("Not Weird")

