ingredient ="\nTell me what do you want to add in your pizza:" 
ingredient += "(Enter 'quit' to stop making your pizza)"
i = ""

'''
while i != 'quit':
	i = input(ingredient)
	if i != "quit":
	    print("We will add " + i + " in your pizza")

else:
	print("Wait for your pizza now,please")
'''

'''
active = True
while active:
  i = input(ingredient)
  if i != "quit":
    print("We will add " + i + " in your pizza")
  else:
    active = False
'''
'''
while i != 'quit':
	i = input(ingredient)
	if i == "quit":
		break
	else:
	    print("We will add " + i + " in your pizza")
   
'''
while i != 'quit':
	i = input(ingredient)
	if i != "quit":
	    print("We will add " + i + " in your pizza")
	else:
	    break
