

def decide(threshold, studentsTiming):
	numberOfStudentsBeforeLecturesDecides = 0
	for studentTime in studentsTiming:
		if studentTime <= 0:
			numberOfStudentsBeforeLecturesDecides += 1
	# print numberOfStudentsBeforeLecturesDecides
	if numberOfStudentsBeforeLecturesDecides >= threshold:
		print "NO"
	else:
		print "YES"

T = int(raw_input()) 
for i in xrange(T):
	caseInfo = raw_input().rstrip().split()
	numberOfStudents = int(caseInfo[0])
	threshold = int(caseInfo[1])
	studentsTiming = raw_input().rstrip().split()
	studentsTiming = map(int, studentsTiming)
	decide(threshold, studentsTiming)


