def isKaprekar(number):
	if number == 1:
		return True
	elif number < 8:
		return False
	squaredString = str(number ** 2)
	squaredStringLength = len(squaredString)
	if squaredStringLength % 2 == 0 :
		l = int(squaredString[:squaredStringLength/2])
		r = int(squaredString[squaredStringLength/2:])
	else:
		# print squaredString
		l = int(squaredString[:squaredStringLength/2])
		r = int(squaredString[(squaredStringLength-1)/2:])
		# print l
		# print r

	if r + l == number:
		return True
	return False

p = int(raw_input())
q = int(raw_input())

kaprekarNumbers = []

for number in xrange(p, q+1):
	if isKaprekar(number):
		kaprekarNumbers.append(number)

if not kaprekarNumbers:
	print "INVALID RANGE"
else:
	print " ".join(str(number) for number in kaprekarNumbers)