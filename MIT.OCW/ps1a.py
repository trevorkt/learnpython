# Problem Set 1, Problem 1
# Trevor T

import math # for sqrt()

def isprime(n):
	'''check if integer n is prime'''

	# make sure n is a positive integer
	n = abs(int(n))

	# 0 and 1 are not primes
	if n < 2:
		return False

	# 2 is the only even prime number
	if n == 2:
		return True

	# all other even numbers are not prime
	if (n/2)*2 == ((n*1.0)/2)*2:
		return False

	# range starts with 3 and skips even numbers
	# only must go up to the square root of n
	endval = int(math.sqrt(n))+1
	for divisor in range(3, endval, 2):
		if n % divisor == 0:
			return False
	return True

primes = []
x = 0
while len(primes) < 1000:
	if isprime(x) == True:
		primes.append(x)
	x += 1
print primes[999],'is the 1,000th prime number.'