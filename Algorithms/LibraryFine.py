actualDate  = raw_input().rstrip()
expectedDate = raw_input().rstrip()

actualDate = actualDate.split()
expectedDate = expectedDate.split()

actualDay = int(actualDate[0])
actualMonth = int(actualDate[1])
actualYear = int(actualDate[2])

expectedDay = int(expectedDate[0])
expectedMonth = int(expectedDate[1])
expectedYear = int(expectedDate[2])

fine  = 0
if actualYear > expectedYear:
	fine = 10000
elif actualMonth > expectedMonth and actualYear == expectedYear:
	fine = 500 * (actualMonth - expectedMonth)
elif actualMonth == expectedMonth and actualDay > expectedDay and actualYear == expectedYear:
	fine = 15 * (actualDay - expectedDay)
elif actualDate <= expectedDate and actualMonth == expectedMonth and actualYear == expectedYear:
	fine = 0 

print fine