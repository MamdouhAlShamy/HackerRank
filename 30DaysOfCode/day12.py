class Student:
    def __init__(self,firstName,lastName,phone):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
    def display(self):
        print "First Name:",self.firstName
        print "Last Name:",self.lastName
        print "Phone:",self.phone

class Grade(Student):
	def __init__(self,firstName,lastName,phone, grade):
		Student.__init__(self, firstName, lastName, phone)
		self.grade = grade
	def calculate(self):
		if self.grade < 40:
			return "D"
		elif self.grade >= 40 and self.grade < 60:
			return "B"
		elif self.grade >= 60 and self.grade < 75:
			return "A"
		elif self.grade >= 75 and self.grade < 90:
			return "E"
		elif self.grade >= 90 and self.grade < 100:
			return "O"
	def display(self):
		Student.display(self)
		print "Grade:", self.calculate()
	

g = Grade("m", "s", 1, 70)
g.display()