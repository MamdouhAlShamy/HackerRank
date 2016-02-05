def isPangram(inp):
 	letters = []
 	for letter in inp:
 		letter = letter.lower()
 		if letter not in letters:
 			letters.append(letter)
 	if len(letters) < 27:
 		print "not pangram"
 	else:
 		print "pangram"
 	# print len(letters)

inp = raw_input()
isPangram(inp)