# Problem Set 1, Problem 1
# Trevor T

import math # for sqrt()

def isprime(x):
	x = abs(int(x))
	if x < 2:
		return False
	if x == 2:
		return True
	if (x/2)*2 == ((x*1.0)/2)*2:
		return False
	for div in range(3, int(math.sqrt(x)), 2):
		if x % div == 0:
			return False
	return True

x = int(raw_input('Enter a positive integer: '))

print isprime(x)