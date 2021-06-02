#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def remove_all_before(items: list, border: int):
	if border in items:
		for i in range(len(items)):
			if items[i] == border:
				return items[i:]	
	return items

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#

#def remove_all_before(items: list, border: int):
	#return items[items.index(border):] if border in items else items		
	
#exception handling solution
#try:
	#return items[items.index(border):]
#except ValueError:
	#return items	

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = []
k = [1, 1, 2, 2, 3, 3]
s = [7, 7, 7, 7, 7, 7, 7, 7, 7]
c = remove_all_before(a, 4)
d = remove_all_before(b, 3)
m = remove_all_before(a, 9)
j = remove_all_before(k, 2)
r = remove_all_before(s, 7)
print(c)
print(d)	
print(m)
print(j)
print(r)