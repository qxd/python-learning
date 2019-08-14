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

user = User('韩','商言')
print(user.describe_user())
print(user.greet_user())
print(user.insrement_login_attempts())
print(user.reset_login_attempts())

user_1 = User('陈','伟霆')
print(user_1.describe_user())
print(user_1.greet_user())

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = ["can delete",'can add','love you']

	def show_privilege(self):
		return self.first_name + self.last_name + '权限有' + self.privileges[2]

adminer = Admin('胡','歌')
print(adminer.show_privilege())


