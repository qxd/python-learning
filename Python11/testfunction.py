
# name.py
def get_formatted_name(first, last, middle=''):
	if middle:

		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' '  + last

	return full_name.title()

# 测试name.py
import unittest
# form testfunction import get_formatted_name
# 新建一个类，继承 unittest.TestCase
class NameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('jains','jopin')

		# 断言
		self.assertEqual(formatted_name,'Jains Jopin')

# 运行测试
unittest.mdev

