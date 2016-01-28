actualDate  = raw_input().rstrip()
expectedDate = raw_input().rstrip()

# actualDate = "9 7 2018"
# expectedDate = "6 6 2015"

actualDate = actualDate.split()
expectedDate = expectedDate.split()

actualDay = int(actualDate[0])
actualMonth = int(actualDate[1])
actualYear = int(actualDate[2])

expectedDay = int(expectedDate[0])
expectedMonth = int(expectedDate[1])
expectedYear = int(expectedDate[2])

# print actualDay, actualMonth, actualYear
# print expectedDay, expectedMonth, expectedYear


fine  = 0
# if actualDate <= expectedDate and actualMonth == expectedMonth and actualYear == expectedYear:
# 	fine = 0
# elif actualMonth == expectedMonth and actualYear == expectedYear:
# 	 fine = 15 * (actualDay - expectedDay)
# elif actualMonth > expectedMonth and actualYear == expectedYear:
# 	fine = 500 * (actualMonth - expectedMonth)
# elif actualYear > expectedYear:
# 	fine = 10000
# else:
# 	fine = -1

if actualYear > expectedYear:
	fine = 10000
elif actualMonth > expectedMonth:
	fine = 500 * (actualMonth - expectedMonth)
elif actualMonth == expectedMonth and actualDay != expectedDay:
	fine = 15 * (actualDay - expectedDay)
elif actualDate <= expectedDate:
	fine = 0 

print fine