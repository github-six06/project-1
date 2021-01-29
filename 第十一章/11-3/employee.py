class Employee():
	def _init_(self,first_name,last_name,salary):
		self.first_name=first_name
		self.last_name=last_name
		self.salary=salary
	def give_raise(self,up=''):
		self.salary=salary
		if up:
			self.salary+=up
		else:
			self.salary+=5000
		return self.salary
