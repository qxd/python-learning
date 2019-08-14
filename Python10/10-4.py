
i = 0
while i < 4:
	with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt', 'a') as file_object:
		name = input('input your name :\n(enter "quit" to end ：）')
		if name == 'quit':
			break
		else:
			file_object.write('\n' + name + '\n')
			i=i+1



