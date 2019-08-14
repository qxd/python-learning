#创建类Dog
class Dog():
	#__init__()是特的方法，创建实例时候默认调用，是两个下划线哦！
	def __init__(self, name, age):
		'初始化狗的名字，年龄'
		self.name = name
		self.age = age
	def sit(self):
		'小狗坐下'
		print(self.name.title() + " is now sitting!")
	def  roll_over(self):
		'小狗打滚'
		print(self.name.title() + " rollled over!")

#根据类创建实例，访问两个属性
my_dog = Dog('qxd', 4)
print("my dog's name is " + my_dog.name + " and it is " + str(my_dog.age) + " yeas old.")

#调用方法
my_dog.sit()

my_dog.roll_over()
