#参数可选择，先制定一个默认值-空字符串
def make_album(singerName, albumName, songNum=''):
	if songNum:
		result = "The " + albumName + " is of " + singerName + " with " + songNum + " songs!"
	else:
		result =  "The " + albumName + " is of " + singerName
	return result

print(make_album("Jay", "七里香", "10"))

print(make_album("Linjunjie", "背对背拥抱"))