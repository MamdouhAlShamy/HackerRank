w1 = list(raw_input().rstrip())
w2 = list(raw_input().rstrip())

count = 0

for letter in w1:
	if letter in w2:
		w2.remove(letter)
	else:
		count += 1
		

count += len(w2)
print count