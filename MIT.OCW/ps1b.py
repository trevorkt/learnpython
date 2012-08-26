# Problem Set 1, Problem 1
# Trevor T

import math # for sqrt() and log()

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

# set variables to exist
primes = []
x = 0

# let user enter how many prime numbers to calculate
usernum = abs(int(raw_input('Create a list of prime numbers up to this int: ')))

# run isprime() function until list has user-specified number of items
while len(primes) < usernum:
	if isprime(x) == True:
		primes.append(x)
		print x
	x += 1
	
# print last item in list	
print primes[usernum - 1],'is the %dth prime number.' % usernum

# give user option to quit program now
userentry = raw_input('Continue? Q to Quit: ')
if userentry == 'Q':
	exit()

# Problem Set 1, Problem 2
# Trevor T

# define function to find product of list items
def product(list):
	prod = 1
	for item in list:
		prod *= item
	return prod

# create variable
primelogs = []

# create list of primes' logs from list of primes
for prnumitem in primes:
	prlogitem = math.log(prnumitem)
	primelogs.append(prlogitem)

# assign sum to variables
logsum = sum(primelogs)
lastprlogitem = primelogs[usernum - 1]

# i don't think i understand the math that i'm supposed to have replicated here
print logsum - lastprlogitem
print usernum
print (logsum - lastprlogitem) / usernum,'\n'
print logsum / usernum,'\n'