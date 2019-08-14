class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		# 初始化属性name和type
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number = 0

	def describe_restaurant(self):
		return "This is a restaurant of " + self.cuisine_type + " cuisine. Its name is " + self.restaurant_name + "."
	def open_restaurant(self):
		print("We are opened,Welcome!")
	def number_served(self,number):
		self.number = number
		return '就餐人数' + str(self.number)



#通过方法修改属性值

restaurant_2 = Restaurant('蚍蜉','粤菜')
print(restaurant_2.describe_restaurant())
restaurant_2.open_restaurant()
print(restaurant_2.number_served(300))


# 子类括号里面包含父类名称
class IcecreamStand(Restaurant):
	# 接受父类信息，
	def __init__(self,restaurant_name,cuisine_type):
		# 关联父类和子类，初始化父类的属性
		super().__init__(restaurant_name,cuisine_type)
		#新增口味属性
		self.flvor = ['香草','巧克力']

icecream = IcecreamStand('wqw','eqeq')

print(icecream.flvor)
