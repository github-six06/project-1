import unittest
from city_functions1 import city_country_population
class CitysTestCase(unittest.TestCase):
	def test_city_country_population(self):
		"""deal with message such as Santiago Chile"""
		name=city_country_population('santiago', 'chile')
		self.assertEqual(name,'Santiago Chile')
unittest.main()
