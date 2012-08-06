# import argv from sys module

from sys import argv

# unpack argv to two variables

script, filename = argv

# open 'filename', defined above via argv,
# and assign contents to variable 'txt'

file_object = open(filename)

# print text & variable 'filename'

print "Here's your file %r: " % filename

# print the output of running the read
# command with no parameters on variable
# 'file_object' (which, remember contains the
# contents of 'filename')

print file_object.read()

# require input from user of the next
# file to be opened, read, and printed
# (assumedly the same file), and set
# user input to variable 'filename_again'

print "Type the filename again:"
filename_again = raw_input("> ")

# set variable 'file_object_again' to contents
# of 'filename_again' via open command

file_object_again = open(filename_again)

# print output of running read command
# on variable 'file_object_again'

print file_object_again.read()

# close both files when finished

file_object.close()
file_object_again.close()