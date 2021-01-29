import unittest	
from EmployeeSurver import Employee
class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.EmployeeTest=Employee('yundan','zeng',10000)
	
	def test_give_default_raise(self):
		self.EmployeeTest.give_raise()
		self.assertEqual(self.EmployeeTest.salary,15000)
	
	def test_give_custom_raise(self):
		self.EmployeeTest.give_raise(10000)
		self.assertEqual(self.EmployeeTest.salary,20000)
unittest.main()			

