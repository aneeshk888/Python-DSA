def powMod(x,n,M):
	res=1


	while n>=1:
		if n%2==1:
			res=(res*x)%M
			n-=1
		else:
			x=(x*x)%M
			n//=2
	return res


if __name__ == "__main__":
    x,n,M=3,2,4
    print(powMod(x,n,M))
