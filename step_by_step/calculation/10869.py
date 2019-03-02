def sum(a,b):
	result = a+b
	return result

def sub(a,b):
	result = a-b
	return result

def mul(a,b):
	result = a*b
	return result

def div(a,b):
	result = int(a/b)
	return result

def rem(a,b):
	result = a%b
	return result

inp=input().split(" ")

a=int(inp[0])
b=int(inp[1])

print(sum(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(rem(a,b))