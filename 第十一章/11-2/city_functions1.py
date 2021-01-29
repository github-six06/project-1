def city_country_population(city_name,country_name,population=''):
	"""describle a city and it's belonging country:"""
	if population:
		message=city_name+','+country_name+'-'+population
	else:
		message=city_name+' '+country_name
	return message.title()
