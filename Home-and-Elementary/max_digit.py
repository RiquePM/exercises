#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def max_digit(number: int): 
	return max(str(number))

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#max_digit = lambda number: int(max(str(number)))

#--------Simple explanation of lambda functions--------#
						
#def name(whatever arguments): → lambda whatever arguments: some expression
    #return some expression --------------------------------------↑


#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#

a = max_digit(52)
print(a)	
