#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def all_the_same(elements: list):
	for i in range(len(elements)):
		if elements[i] != elements[i-1]:
			return False
	return True		
 
#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#

#def all_the_same(elements):
#	return elements[1:] == elements[:-1]

#def all_the_same(elements):
#	return len(set(elements)) <= 1

#def all_the_same(elements):
    #return all(elements[0] == e for e in elements[1:])

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = all_the_same([1, 1, 1]) #== True
b = all_the_same([1, 2, 1]) #== False
c = all_the_same(['a', 'a', 'a']) #== True
d = all_the_same([]) #== True
e = all_the_same([1]) #== True	
print(a, b, c, d, e, sep="\n")
