class Node:
	def __init__(self,init__data):
		self.data =init_data
		self.next= None

	def get_data(self):
		return self.data
	def get_next(self):
		return self.next

	def set_data(self,new_data):
		self.data= newdata
	
	def set_next(self,new_next):
		self.next = new_next
