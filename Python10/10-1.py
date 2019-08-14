
#读取整个文件
with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt') as file_object:
	print(file_object.read().rstrip())

# 一行一行读取
file_name = '/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt'
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())


# readlines()读取每行bong存储到一个列表中
file_name = '/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()
	for line in lines:
		print(line.rstrip())
