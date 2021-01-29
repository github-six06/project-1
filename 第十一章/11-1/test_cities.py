import unittest
from city_functions import city_country_name
class CitysTestCase(unittest.TestCase):
	def test_city_country_name(self):
		"""deal with message such as Santiago Chile"""
		name=city_country_name('santiago', 'chile')
		self.assertEqual(name,'Santiago Chile')
unittest.main()		
