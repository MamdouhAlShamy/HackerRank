
class Difference:
	
	def __init__(self, a):
		self.__elements = a
		self.maximumDifference = 0
	def computeDifference(self):
		for i in range(0, len(self.__elements) - 1):
			for j in range(i+1, len(self.__elements)):
				res = abs(self.__elements[i] - self.__elements[j])
				# print "res: ", res
				# print "max: ", self.maximumDifference
				if self.maximumDifference < res:
					self.maximumDifference = res

        		




a = [8, 19, 3, 2, 7]
d = Difference(a)
d.computeDifference()

print d.maximumDifference