from sys import argv

script, filename = argv

file_object = open(filename, 'w')

file_object.close()