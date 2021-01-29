import unittest
from city_functions1 import city_country_population
class CitysTestCase(unittest.TestCase):
	def test_city_country_population(self):
		message=city_country_population('santiago','chile','population=5000000')
		self.assertEqual(message,'Santiago,Chile-Population=5000000')
unittest.main()
