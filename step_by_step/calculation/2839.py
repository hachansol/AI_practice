N=int(input())

count = int(N/5) #몫 
remain = N%5 # 나머지 
if N==4:
	print(-1)
elif N==7:
	print(-1)
else:
	if remain == 0:
		print(count)
	elif remain == 1 or remain == 3:
		print(count+1)
	elif remain == 2 or remain == 4:
		print(count+2)