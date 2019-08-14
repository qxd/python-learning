from 餐馆 import Restaurant

restaurant_2 = Restaurant('群殴活多','川菜')
print(restaurant_2.describe_restaurant())


from 权限 import User, Privileges, Admin
adminer = Admin('胡','歌')
print(adminer.privileges.show_privilege())
print(adminer.privileges.loveornot())