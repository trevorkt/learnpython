# x = 3 # Create variable x and assign value 3 to it x=x*x # Bind x to value 9
# print x
# n = raw_input('Enter a number: ')
# print n
# # print n/n
# 
# x = 15
# if (x/2)*2 == x:
#     print x,'is Even.'
# else: print x,'is Odd.'
# 
# z = 'b'
# if 'x'<z:
#     print 'Hello'
#     print 'Mom'
# 
# x = 15
# y = 5
# z = 11
# print x,y,z
# if x < y and x < z: least_result = x
# elif y < z: least_result = y
# else: least_result = z
# print '%r is least' % least_result

y=0
x=-1
itersLeft = x
while(itersLeft>0):
    y=y+x
    itersLeft = itersLeft - 1
    print 'y =',y,', itersLeft=',itersLeft
print y

# x = 10
# i = 1
# while(i<x):
#     if x%i==0:
#         print 'divisor ', i
#     i = i +1