def rem(a,b):
	result = a%b
	return result

def sum(a,b):
	result = a+b
	return result

def mul(a,b):
	result = a*b
	return result

inp=input().split(" ")

a=int(inp[0])
b=int(inp[1])
c=int(inp[2])

print(rem(sum(a,b),c))
print(rem(sum(rem(a,c),rem(b,c)),c))
print(rem(mul(a,b),c))
print(rem(mul(rem(a,c),rem(b,c)),c))