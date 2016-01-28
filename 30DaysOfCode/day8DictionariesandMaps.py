
inputList = ["sam\r",
			"99912222\r",
			"tom\r",
			"11122222\r",
			"harry\r",
			"12299933\r"
			]

i = 0

def raw_input():
	global i
	i += 1
	return inputList[i-1]


def createPhoneBook():
	N = 3
	phoneBook = {}
	for i in range(N):
		name = raw_input().rstrip()
		number = int(raw_input())
		phoneBook[name] = number
	return phoneBook

def main(phoneBook):
	while True:
		try:
			q = raw_input()
			if q in phoneBook:
				print(q + "=" + phoneBook[q])
			else:
				print("Not found") 
		except EOFError:
			break

phoneBook = createPhoneBook()
main(phoneBook)

res = phoneBook["san"]
print(res)
