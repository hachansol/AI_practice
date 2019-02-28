import sys
sys.setrecursionlimit(10000)

n=int(input())

dp=[None]*46
dp[0]=0
dp[1]=1

def fib(a):
	if dp[a]==None:
		dp[a]=fib(a-1)+fib(a-2)
		return dp[a]
	else:
		return dp[a]

print(fib(n))
