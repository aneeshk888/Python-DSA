def floordiv(a,b):
	return a//b

def ceildiv(a,b):
	return -(-a//b)

def divfloorceil(a,b):
 res=[]
 res.append(floordiv(a,b))
 res.append(ceildiv(a,b))
 return res

if __name__ == "__main__":
 a,b=5,3
 res=divfloorceil(a,b)
 print(res[0],res[1])
