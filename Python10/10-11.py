import json
filename = 'test.json'
nums = ['name','qxd','age','18','favorite','eat']
with open ('test.json','w') as f_obj:
	json.dump(nums,f_obj)
with open ('test.json') as f_obj:
	print(json.load(f_obj)[1])