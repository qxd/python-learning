users = {
	'qxd':{
	'first':'qu',
	'last': 'xiaodan',
	'location':'hangzhou'
	},
	'mw':{
	'first':'ma',
	'last': 'wei',
	'location':'hefei'
	}
}

for user_name, user_info in users.items():
	#print("\n" + "UserName:" + user_name.title() + "\n\tFullname:" + user_info['first'] + " " +  user_info['last'] + "\n\tLocation:" + user_info['location'].title())
    fullname = user_info['first'] + " " + user_info['last']
    print("\nUserName:" + user_name.title())
    print("\tFullname:" + fullname)
    print("\tLocation:" + user_info['location'])
