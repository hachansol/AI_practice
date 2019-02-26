N = int(input())

count = 0

if N<100:
	print(N)

else:
	count = 99
	if N==1000:
		N -= 1

	while N>=100:
		str_n = str(N)
		if int(str_n[0])+int(str_n[2])==2*int(str_n[1]):
			count = count+1
		N -= 1
	print(count)
