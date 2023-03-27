import datetime

from backend.models import Car, Driver, Garage, Manufacturer, Station, Status

test_manufacturer = Manufacturer()
test_driver = Driver()
test_car = Car()
test_garage = Garage()
test_status = Status()
test_station = Station()

test_manufacturer = {
    'id': 1,
    'name': "Nissan",
    'start_date': str(datetime.date(year=1933, month=12, day=26))
}

test_driver = {
    'id': 1,
    'name': "Sanic",
    'birthday': str(datetime.date(year=2010, month=3, day=31))
}

test_car = {
    'id': 1,
    'on': False,
    'doors': 2,
    'color': 'black',
    'make': test_manufacturer,
    'passengers': [test_driver]
}

test_garage = {
    'spaces': 2,
    'cars': [test_car]
}

test_success = {
    'success': True
}

test_station = {
    'contact': 00000000,
    'location': 'Seattle',
}

test_countries = ['South Africa', 'China', 'Syria', 'Tajikistan', 'Indonesia', 'Indonesia', 'Colombia', 'Argentina', 'United States', 'Paraguay', 'Brazil', 'Vietnam', 'Indonesia', 'Philippines', 'Japan', 'Tunisia', 'North Korea', 'Portugal', 'Yemen', 'Russia', 'Canada', 'United States', 'Kazakhstan', 'Japan', 'Sweden', 'Brazil', 'Philippines', 'Poland', 'Thailand', 'Greece', 'China', 'China', 'Mexico', 'Norway', 'Japan', 'Portugal', 'Dominican Republic', 'Philippines', 'Russia', 'Indonesia', 'Indonesia', 'Mexico', 'Ukraine', 'Colombia', 'China', 'Poland', 'Poland', 'Macedonia',
                  'Indonesia', 'Sweden', 'Libya', 'Mexico', 'Poland', 'Armenia', 'Peru', 'Yemen', 'Greece', 'Indonesia', 'Russia', 'Yemen', 'Luxembourg', 'Japan', 'Tajikistan', 'China', 'Philippines', 'Nigeria', 'Colombia', 'Pakistan', 'Peru', 'Ukraine', 'Canada', 'Indonesia', 'Indonesia', 'China', 'Greece', 'Poland', 'China', 'China', 'Belarus', 'Portugal', 'China', 'Brazil', 'Indonesia', 'China', 'Russia', 'Indonesia', 'China', 'Philippines', 'Indonesia', 'Argentina', 'China', 'Colombia', 'China', 'Thailand', 'Thailand', 'Cambodia', 'Indonesia', 'Philippines', 'Thailand', 'China']

test_car_makes = ['Ford', 'Chevrolet', 'Dodge', 'Toyota',
                  'Honda', 'BMW', 'Mercedes-Benz', 'Audi', 'Porsche', 'Tesla']
