def make_shirt(size, logo="bala"):
	print("The size I need is " + size + "，and logo is " + logo)

#位置实参
make_shirt("XL", "飞修")

#关键字实参
make_shirt(logo="feixiu测试部", size="M")

#默认值

make_shirt(size="XXXL",logo="I love Python")

make_shirt(size="L",logo="I love Python")

make_shirt(size="L")

