#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def end_zeros(num: int):
	num_str = str(num)
	count = 0
	for i in num_str[::-1] :
		if i == "0":
			count += 1
		else:
			break
	return count

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#
#def end_zeros(num: int) -> int:
    #s = str(num)
    #return len(s) - len(s.rstrip('0'))

#def end_zeros(number):
    #import re
    #return len(re.search('0*$', str(number)).group(0))

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#
a = end_zeros(0) # == 1
b = end_zeros(1) # == 0
c = end_zeros(10) # == 1
d = end_zeros(101) # == 0
e = end_zeros(245) # == 0
f = end_zeros(100100) # == 2
print(a, b, c, d, e, f, sep="\n")