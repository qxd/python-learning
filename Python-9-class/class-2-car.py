class Car():
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year
		#给属性指定默认值
		self.odometer = 1000

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.brand + ' ' + self.model
		return long_name.title()

	def get_decriptive_odometer(self):
		print("This car has " + str(self.odometer) + " miles on it.")
	#更新
	def update_odometer(self, mileage):
		self.odometer = mileage
	#递增方法
	def increment_odometer(self, mile):
		self.odometer += mile

#实例
my_new_car = Car('audi', 'a4', 2018)

#方法调用
print(my_new_car.get_descriptive_name())
my_new_car.get_decriptive_odometer()

#直接修改属性的值
my_new_car.odometer = 2000
my_new_car.get_decriptive_odometer()

#通过方法修改属性值。先定义一个内部更新属性的方法
my_new_car.update_odometer(23)
my_new_car.get_decriptive_odometer()

#通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.get_decriptive_odometer()

#类的继承
#class的继承，新建父类Car类的子类ElectricCar
class ElectricCar(Car):
	def __init__(self, brand, model, year):
		'''初始化父类的属性'''
		super().__init__(brand, model, year)
		self.battery_size = 70

	def describe_battery(self):
		print("This has a " + str(battery_size) + "kWh battery")

my_new_car_2 = ElectricCar('baoma', 'S4', 2018)
print(my_new_car_2.get_descriptive_name())

print(my_new_car_2.describe_battery())

