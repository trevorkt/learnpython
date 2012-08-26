from sys import argv

script, A = argv

def print_all(B):
	print B.read()

def rewind(B):
	B.seek(0)

def print_a_line(B):
	print B.readline(),

D = open(A)

print "First let's print the whole file:\n"

print_all(D)

print "Now let's rewind, kind of like a tape."

rewind(D)

print "Let's print three lines:"

print_a_line(D)

print_a_line(D)

print_a_line(D)