N  = int(raw_input())
message = raw_input()
K = int(raw_input())

# message = "AZaz"
# K = 100
encryptedMessage = ""
while K > 26:
	K = K - 26
for letter in message:
	asciiValue = ord(letter) 
	if asciiValue >= 65 and asciiValue <= 90:
		newAsciiValue = asciiValue + K
		if newAsciiValue > 90:
			newAsciiValue -= 26
		encryptedMessage += chr(newAsciiValue)
	elif asciiValue >= 97 and asciiValue <= 122:
		newAsciiValue = asciiValue + K
		if newAsciiValue > 122:
			newAsciiValue -= 26
		encryptedMessage += chr(newAsciiValue)
	else:
		encryptedMessage += letter
print encryptedMessage