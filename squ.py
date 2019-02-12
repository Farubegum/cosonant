san=int(input())
sam=0
while(san>0):
	d=san%10
	sam=sam+(d*d)
	san=san//10
print(sam)
