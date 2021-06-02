#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def backwards_string(val: str):
	val_list = list(val)
	c = list.reverse(val_list)
	rev_str = "".join(val_list)
	return rev_str

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#

#def backward_string(val: str):
	#return val [::-1]

#backward_string = lambda val: val[::-1]

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

k = backwards_string("Henrique")
print(k)	
