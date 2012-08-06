# import argv from sys module
from sys import argv

# unpack argv to two variables
script, filename = argv

# open 'filename', defined above via argv,
# and assign contents to variable 'txt'
txt = open(filename)

# print text & variable 'filename'
print "Here's your file %r: " % filename

# print the output of running the read
# command with no parameters on variable
# 'txt' (which, remember contains the
# contents of 'filename')
print txt.read()

print "Type the filename again:"
# require input from user of the next
# file to be opened, read, and printed
# (assumedly the same file), and set
# user input to variable 'file_again'
file_again = raw_input("> ")

# set variable 'txt_again' to contents
# of 'file_again' via open command
txt_again = open(file_again)

# print output of running read command
# on variable 'txt_again'
print txt_again.read()