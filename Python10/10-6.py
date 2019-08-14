
try:
	print(4/0)
except ZeroDivisionError:
	print('分母不能为0')
try:
	with open('10') as file_object:
		print(file_object.read())
except FileNotFoundError:
	print('未找到该文件')
i = 0
sum = 0
while i < 2:
	try:
		num_1 = int(input('请输入第一个数字：'))
		num_2 = int(input('请输入第二个数字：'))

		i += 1
		sum = sum + num_1 + num_2

	except ValueError:
		pass
		# print('输入的不是整数，无法相加')

print(sum)