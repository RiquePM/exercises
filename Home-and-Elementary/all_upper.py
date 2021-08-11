#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
import re

def is_all_upper(text: str):
	if re.search("[a-z]", text):
		return False
	return True		

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#def is_all_upper(text: str) -> bool:
    #return text.upper() == text

#import string
#def is_all_upper(text: str) -> bool:
    #return all(c not in string.ascii_lowercase for c in text)

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
