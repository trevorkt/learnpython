# define function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print first line, cheese variable
	print "You have %d cheeses!" % cheese_count
	# print second line, crackers variable
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# print third line..
	print "Man that's enough for a party!"
	# print fourth line..
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# run function w/ 20 cheese count and 30 crackers count
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
# set cheese count and cracker count
amount_of_cheese = 10
amount_of_crackers = 50

# run function with above set counts
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# run cheese and crackers with simple arithmetic setting variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# run cheese and crackers with above set counts and arithmetic
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)