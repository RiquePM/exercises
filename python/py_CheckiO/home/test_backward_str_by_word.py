import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def backward_str_by_word(text):
	txt_list = [word[::-1] for word in text.split(" ")]
	return " ".join(txt_list)

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#return " ".join(word[::-1] for word in text.split(" "))

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBackwarStrByWord(unittest.TestCase):
	def test_empty_string(self):
		self.assertEqual(
			backward_str_by_word(''), '')	

	def test_backward_single_word(self):
		self.assertEqual(
			backward_str_by_word('world'), 'dlrow') 

	def test_backward_two_words(self):
		self.assertEqual(
			backward_str_by_word('hello world'), 'olleh dlrow') 
    
	def test_double_blank_space_between_words(self):
		self.assertEqual(
			backward_str_by_word('hello   world'), 'olleh   dlrow') 
    
	def test_backward_string(self):
		self.assertEqual(
			backward_str_by_word('welcome to a game'), 'emoclew ot a emag') 


if __name__ == '__main__':
	unittest.main()
