with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt') as file_object:
	# print(file_object.read())
	message = file_object.read().replace ('Python','C')
	print(message)

