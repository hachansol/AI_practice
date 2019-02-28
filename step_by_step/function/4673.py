def self(number):
	sum=0
	for i in str(number):
		sum += int(i)

	result=sum+number
	return result

dp=[0]*10000

for i in range(10000):
	value=self(i)
	if value <10000:
		dp[value]=1

for j in range(10000):
	if dp[j]==0:
		print(j)