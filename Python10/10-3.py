name = input('enter your name :')
with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt','a') as file_object:
	file_object.write(name + '\n')
	file_object.write('lixian love you !')
# with open('/Users/quxiaodan/Documents/python_work/python从入门到实践/Python10/learning_python.txt','a') as file_object:
# 	file_object.write(name + '\n')
# 	file_object.write('cwt love you !')
