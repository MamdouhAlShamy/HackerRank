N = int(raw_input())
inp = raw_input()
inp = inp.rstrip()
inp = inp.split()
inp = map(int, inp)

# print inp

# N = 4
# inp = [5, 4, 3, 2]

# inp.sort()

# diff = abs(inp[0]-inp[1])
# st = []

# for i in xrange(N-1):
# 	for j in xrange(i+1, N):
# 		val = abs(inp[i] - inp[j])
# 		if val == diff:
# 			st.append(inp[i])
# 			st.append(inp[j])
# 		elif val < diff:
# 			diff = val
# 			del st[:]
# 			st.append(inp[i])
# 			st.append(inp[j])

# # print ' '.join(str(x) for x in sorted(st))
# print ' '.join(str(x) for x in st)


inp.sort()

diff = abs(inp[0] - inp[1])
st = []

for i in xrange(N-1):
	val = abs (inp[i] - inp[i+1])
	if val == diff:
		st.append(inp[i])
		st.append(inp[i+1])
	elif val < diff:
		diff = val
		del st[:]
		st.append(inp[i])
		st.append(inp[i+1])

# print ' '.join(str(x) for x in sorted(st))
print ' '.join(str(x) for x in st)