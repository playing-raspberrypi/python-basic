
from car import car

# OOP - Flying car inheritence from Car

class flying_car(car):
	def __init__(self, brand_name, model, is_light_space_available = False):
		self.brand_name = brand_name
		self.model = model
		self.is_light_space_available = is_light_space_available

	def print_flying_car(self):
		self.print_car()

		if self.is_light_space_available :
			print('It can travel with speed of light')
		else :
			print('It cannot travel with speed of light')

#-------------------------------------------------------------------a

tesla_flying_car = flying_car('Tesla', 'FLY 2021', True)
tesla_flying_car.print_flying_car()

tesla_flying_car2 = flying_car('Tesla', 'FLY 2021', False)
tesla_flying_car2.print_flying_car()

tesla_flying_car3 = flying_car('Tesla', 'FLY 2021')
tesla_flying_car3.print_flying_car()