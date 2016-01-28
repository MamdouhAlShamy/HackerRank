class Palindrome:
	def __init__(self):
		self.stack = []
		self.queue = []

    def pushCharacter(ch):
    	self.stack.append(ch)
    
    def enqueueCharacter(ch):
    	self.queue.append(ch)

    def popCharacter():
    	ch = self.stack[-1]
    	del self.stack[-1]
    	return ch

    def dequeueCharacter():
    	ch = self.queue[0]
    	del self.queue[0]
    	return ch
