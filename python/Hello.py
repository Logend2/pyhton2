import random
s = random.randint(1,10)
i = 0
while i != 4 :

	temp = input("请输入\n")
	a = int(temp)
        
	if a > s :
		print("大了，老哥")
		print("还有%d次机会"%(3-i))
		i += 1
	elif a < s :
		print("小了，吗？，兄die")
		print("还有%d次机会" % (3-i))
		i += 1
	else :
		print("可以的，对了")
		break
print("溜了")
