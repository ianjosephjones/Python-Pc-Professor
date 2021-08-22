"""
Exercise 6-11
-------------
Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
dictionary of information about each city and include the country that the city is in, its approximate
population, and one fact about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored
about it.
"""

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    print(f"\n{city.title()} is in {country}.")
    print(f" It has a population of about {population}.")
    print(f" The {mountains} mounats are nearby.")

"""
Output:
-------
Santiago is in Chile.
It has a population of about 6310000.
The Andes mounats are nearby.
Talkeetna is in United States.
It has a population of about 876.
The Alaska Range mounats are nearby.
Kathmandu is in Nepal.
It has a population of about 975453.
The Himilaya mounats are nearby
"""
