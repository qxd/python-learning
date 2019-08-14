#8-8
def make_album(singerName, albumName, songNum=''):
	if songNum:
		result = "The " + albumName + " is of " + singerName + " with " + songNum + " songs!"
	else:
		result =  "The " + albumName + " is of " + singerName
	return result

while True:
	print("Please enter the singer's Name：")
	singerName = input("singer Name: ")
	if singerName == "quit":
		break
	else:
		albumName = input("album Name: ")
	print(make_album(singerName,albumName))
