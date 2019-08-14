#待优化
ask = "0"
ask = int(ask)
while ask <= 12:
	ask = input("Tell me, How old are you?")
	ask = int(ask)
	if ask < 3:
		print("Congratulations! You are free！")
	if ask >= 3 and ask <= 12:
		print("Pay me $10 please!Thank you.")
else:
    print("Pay me $15 please!Thank you.")