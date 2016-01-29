h = int(raw_input().strip())
m = int(raw_input().strip())

# h = 5
# m = 45

dictinary= {1: "one",
			2: "two",
			3: "three",
			4: "four",
			5: "five",
			6: "six",
			7: "seven",
			8: "eight",
			9: "nine",
			10: "ten",
			11: "eleven",
			12: "twelve",
			13: "thirteen",
			14: "fourteen",
			15: "quarter",
			16: "sixteen",
			17: "seventeen",
			18: "eighteen",
			19: "nineteen",
			20: "twenty",
			40: "twenty",
			21: "twenty one",
			22: "twenty two",
			23: "twenty three",
			24: "twenty four",
			25: "twenty five",
			26: "twenty six",
			27: "twenty seven",
			28: "twenty eight",
			29: "twenty nine"
			}

if m == 0:
	string = dictinary[h] + " o' clock"
elif m < 30:
	if m == 1:
		string = dictinary[m] + " minute past " + dictinary[h]
	elif m == 15:
		string = dictinary[m] + " past " + dictinary[h]
	else:
		string = dictinary[m] + " minutes past " + dictinary[h]
elif m == 30:
	string = "half past " + dictinary[h]			
elif m > 30:
	m = 60 - m
	if m == 59:
		string = dictinary[m] + " minute to " + dictinary[h+1]
	elif m == 15:
		string = dictinary[m] + " to " + dictinary[h+1]
	else:
		string = dictinary[m] + " minutes to " + dictinary[h+1]


print string
