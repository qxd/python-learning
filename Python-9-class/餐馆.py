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


#直接修改变量值
# restaurant_1 = Restaurant('红顶','徽菜')
# restaurant_1.number = 200
# print(restaurant_1.describe_restaurant())
# restaurant_1.open_restaurant()
# print(restaurant_1.number_served())

#通过方法修改属性值

restaurant_2 = Restaurant('蚍蜉','粤菜')
print(restaurant_2.describe_restaurant())
restaurant_2.open_restaurant()
print(restaurant_2.number_served(300))



# restaurant_3 = Restaurant('雀罗活多','西域菜')
# print(restaurant_3.describe_restaurant())
# restaurant_3.open_restaurant()

