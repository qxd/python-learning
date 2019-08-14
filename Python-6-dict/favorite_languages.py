# 字典dict里面存储列表list
favorite_languages = {
	'qxd':['Python', 'JS', 'HTML'],
	'mawei':['C'],
	'fangteng':['Python', 'Selenium']
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
	  print("\n" + name.title() + "`s favorite language is:")  
	else:
		print("\n" + name.title() + "`s favorite language are:")  
	for language in languages:
		print("\t" + str(language))