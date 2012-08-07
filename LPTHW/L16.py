from sys import argv

script, filename = argv

print "# We're going to erase %s." % filename
print "# If you don't want that, hit CTRL-C."
print "# If you do want that, hit Return."

raw_input("> ")

print "# Opening your file...\n"
target = open(filename, 'r+')

print "# This is your file,\n"

print target.read()

print "# Are you sure you want to erase it?\n"
print "# If no, hit CTRL-C."
print "# If yes, hit Return."

raw_input("> ")

print "# Truncating the file. Goodbye data!"

target.truncate(0)

print "# Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "# And I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "# And finally, we close it."
target.close()

print "# Would you like to read another file?\n"
print "# If no, hit CTRL-C."
print "# If yes, enter its filename."

filename2 = raw_input("> ")

target2 = open(filename2)

print "# And here is that file.\n"

print target2.read()

print "# Goodbye!"

target2.close()