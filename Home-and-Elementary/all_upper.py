#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def is_all_upper(text: str):
	if text == '':
		return True	
	return text.isupper() or text.isspace() or text.isnumeric()

#--------------------------------------------#
#	      Other Solutions	     	     #
#--------------------------------------------#

#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#

print(is_all_upper('AARRR')) #True	
print(is_all_upper('adka')) #False
print(is_all_upper('mixed UPPER and lower')) #False
print(is_all_upper('')) #True
print(is_all_upper('     ')) #True
print(is_all_upper('444')) #True
print(is_all_upper('55 55 5')) #True
