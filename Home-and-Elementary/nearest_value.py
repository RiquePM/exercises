#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def nearest_value(values: set, one: int):
	if one in values:
		return one
	sorted_list = list(values)
	sorted_list.sort()
	bigger = [a for a in sorted_list if a > one]
	smaller = [b for b in sorted_list if b < one]
	if not smaller:
		return min(bigger)
	elif not bigger:
		return max(smaller)
	two_nearest = [max(smaller), one, min(bigger)]
	if len(range(two_nearest[0], two_nearest[1]+1)) <= len(range(two_nearest[1], two_nearest[2]+1)):
		return two_nearest[0]
	else:
		return two_nearest[2]

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#
#def nearest_value(values: set, one: int) -> int:
    #return min(values, key=lambda n: (abs(one - n), n))

#def nearest_value(values: set, one: int) -> int:
    #return min((abs(n-one), n) for n in values)[1]

#def nearest_value(values: set, one: int) -> int:
	#return sorted(values, key=lambda x: (abs(x - one), x))[0]

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#
a = nearest_value({4, 7, 10, 11, 12, 17}, 9) #== 10
b = nearest_value({4, 7, 10, 11, 12, 17}, 8) #== 7
c = nearest_value({4, 8, 10, 11, 12, 17}, 9) #== 8
d = nearest_value({4, 9, 10, 11, 12, 17}, 9) #== 9
e = nearest_value({4, 7, 10, 11, 12, 17}, 0) #== 4
f = nearest_value({4, 7, 10, 11, 12, 17}, 100) #== 17
g = nearest_value({5, 10, 8, 12, 89, 100}, 7) #== 8
h = nearest_value({-1, 2, 3}, 0) #== -1
print(a, b, c, d, e, f, g, h, sep = '\n')
