import unittest	
from employee import Employee
class TestEmployee(unittest.TestCase):
	def setup(self):
		self.my_employee=Employee('zeng','yundan','65000')
		#self.first_name='ma'
		#self.last_name='yun'
		#self.annual_salary=65000
	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.asssertEqual(self.my_employee.annual_salary,70000)
	def test_give_custom_raise(self):
		self.my_employee.give_raise(added_salary=10000)
		self.assertEqual(self.my_employee.salary,75000)
unittest.main()			

