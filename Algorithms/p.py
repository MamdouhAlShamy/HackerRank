# x = '123451'
# print x.index('1')

# print [pos for pos, char in enumerate(x) if char == '1']

a = [1,2,3,4,5]

indexesToBeDeleted = []
for i in xrange(len(a)):
	print a[i]
	if i == 3:
		del a[i]

print a
