class Printer:
	def __init__(self,ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(Self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			self.timeRemaining <= 0 :
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False
	def starNext(self,newtask):
		self.currentTask = newTask
		self.timeRemaining= newTask.getPages()*60/self.pagerate	
	
