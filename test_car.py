from car_factory import CarFactory
from datetime import date

carFactory = CarFactory()

print(carFactory.create_calliope(date.today(), date.today(), 70000, 50000).needs_service())
