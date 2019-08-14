from random import randint
class Die:
	def __init__(self,sides = 20):
		self.sides = sides

	def rool_die(self):
		for i in range(0,self.sides):
			print(randint(1,self.sides))


my_die = Die()
my_die.rool_die()
