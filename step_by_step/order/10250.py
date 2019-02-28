T=int(input())

for i in range(T):
	tel=input().split(' ')
	H=int(tel[0])
	N=int(tel[2])

	number=int(N/H)+1
	str_n=str(number)

	floor=N%H
	str_f=str(floor)

	if floor==0:
		str_f=str(H)
		str_n=str(number-1)

	if int(str_n)<10:
		print(str_f+'0'+str_n)
	else:
		print(str_f+str_n)
