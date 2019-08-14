respones = {}

polling_active = True

while polling_active:
	name = input("\nWhat ia your name?")
	mountain = input("Which mountain would you to climb someday?")

	respones[name] = mountain

	repeat = input("Would you like to let another person respond?")
	if repeat == "no":
		polling_active = False

print("\n---Poll Result---")
for name, mountain in respones.items():
	print(name.title() + " would like to climb " + mountain)

