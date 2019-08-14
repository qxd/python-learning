pizza = {
	'crust': 'thick',
	'toppings':['mushroom', 'eatra cheese'],
}
print("You order a" + pizza['crust'] + "-crust pizza" + "with the following topping:")
for topping in  pizza['toppings']:
	print (topping)