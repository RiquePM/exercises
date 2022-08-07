import unittest
import re


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def is_all_upper(text):
	if re.search("[a-z]", text):
		return False
	return True		

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def is_all_upper(text: str) -> bool:
    #return text.upper() == text

#import string
#def is_all_upper(text: str) -> bool:
    #return all(c not in string.ascii_lowercase for c in text)

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestAllUpper(unittest.TestCase):
	def test_is_all_upper(self):
		self.assertTrue(is_all_upper('AARRR'))	

	def test_is_all_lower(self):
		self.assertFalse(is_all_upper('adka')) 

	def test_is_not_all_upper(self):	
		self.assertFalse(is_all_upper('mixed UPPER and lower')) 
    
	def test_is_empty_string(self):
		self.assertTrue(is_all_upper('')) 
    
	def test_blank_space_string(self):
		self.assertTrue(is_all_upper('     ')) 
    
	def test_is_number(self):
		self.assertTrue(is_all_upper('444')) 
    
	def test_is_number_with_blank_spaces(self):
		self.assertTrue(is_all_upper('55 55 5')) 


if __name__ == '__main__':
	unittest.main()