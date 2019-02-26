import sys
T=int(sys.stdin.readline())

for i in range(T):
	inp=sys.stdin.readline().rstrip().split(' ')
	A=int(inp[0])
	B=int(inp[1])
	print(A+B)