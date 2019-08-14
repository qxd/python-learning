def city_and_country(country,city,population=''):
	if population:

		out = country + ',' + city + '-' + '人口 ' + population
	else:
		out = country + ',' + city

	return out.title()

import unittest
class city_and_countryTest(unittest.TestCase):中国,北京-Population
	def test_city_and_country(self):
		city_country = city_and_country('中国','北京')
		self.assertEqual(city_country,'中国,北京')
unittest.main()



