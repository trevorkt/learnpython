from sys import argv

script, from_path, to_path = argv

print "# Duplicating %s to %s ..." % (from_path, to_path)

indata = open(from_path).read()

outfile = open(to_path, 'w').write(indata)

print "# Duplicated."