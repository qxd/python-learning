class User():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		return "His name is " + self.first_name + self.last_name

	def greet_user(self):
		return "Hello,男神,"+ self.first_name + self.last_name
	def insrement_login_attempts(self):
		self.login_attempts += 100
		return '遇见次数' + str(self.login_attempts)

	def reset_login_attempts(self):
		self.login_attempts = 0
		return self.login_attempts

# user = User('韩','商言')
# print(user.describe_user())
# print(user.greet_user())
# print(user.insrement_login_attempts())
# print(user.reset_login_attempts())
#
# user_1 = User('陈','伟霆')
# print(user_1.describe_user())
# print(user_1.greet_user())

# 创建User的子类Admin
class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()
		print(self.first_name + self.last_name)


class Privileges():
	def __init__(self,privileges = 'delete'):
		# self.privileges = ['add','delete','love you']
		self.privileges = privileges

	def show_privilege(self):
		return self.privileges


	def loveornot(self):
		if self.privileges == 'add':
			loveornot = "love you"
			return loveornot
		elif self.privileges == 'delete':
			loveornot = 'really love you'
			return loveornot

# adminer = Admin('胡','歌')
# print(adminer.privileges.loveornot())