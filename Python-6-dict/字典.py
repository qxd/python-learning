#coding:utf-8
alien_0 = {}
alien_0['name'] = 'quxiaodan'
alien_0['birthday'] = '1991-08-11'
alien_0['名族'] = '汉'
alien_0['age'] = '43'
alien_0['age1'] = '43'
#print('名族：' + alien_0['名族'])
#print(alien_0)
'''for key in alien_0.keys():
    print("\nKey是：" + key)

for value in set(alien_0.values()):
	print('Name是：' + value)
'''
#嵌套
'''alien_1 = {'name':'qxd', 'age':'18'}
alien_2 = {'name':'bob','age':'24'}
#字典列表
alien = [alien_0,alien_1,alien_2]
print(alien[0]['name'])'''
# 创建30个外星人
aliens = []
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
	#print(alien)
#输出前5个外星人

print(aliens[0])
# for alien in aliens[:5]:
	# print(alien)
# print("...")
# print("Total number of aliens is: " + str(len(aliens)))
 
for alien in aliens[:3]:
	if alien['color'] =='green':
	   alien['color'] = 'yellow'
	   alien['speed'] = 'medium'
	   alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
# for alien in  aliens[:3]:
	# print(alien)


