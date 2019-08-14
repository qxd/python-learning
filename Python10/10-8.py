try:
	with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/cats.txt',) as file_object:
		print(file_object.read())

	with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/dogs.txt') as file_object:
		print(file_object.read())
except FileNotFoundError:
	print('文件不存在')
except ValueError:
	print('参数错误')