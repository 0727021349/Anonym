def isPrime(n):
	if n < 2:
		return False
	else:
	     for x in range(2, n):
	     	if n % x == 0:
	     		return False
	     	elif x == (n-1):
	     		return n
def primes(p):
	nums = []
	for x in range(0, p+1):
		if isprime(x)
	return nums