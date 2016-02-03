T = raw_input()
T = T.split(":")

hours = int(T[0])
minutes = T[1]
seconds = T[2][0]+T[2][1]
partOfDay = T[2][2] + T[2][3]

# print hours
# print minutes
# print seconds
# print partOfDay

if hours == 12 and partOfDay == "AM":
	hours = "00"
elif partOfDay == "PM" and hours < 12:
	hours = hours + 12

if hours < 10:
	hours = "0" + str(hours)

print str(hours) + ":" + str(minutes) + ":" + str(seconds)
