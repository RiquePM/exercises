import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def count_digits(text):
	a = 0
	for i in text:
		if i.isdigit():
			a += 1
	return a	

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def count_digits(text: str) -> int:
    #return sum(c.isdigit() for c in text)

#import re
#def count_digits(text):
    #return len(re.findall(r"\d", text))
    #return len(re.findall('[0-9]', text))

#def count_digits(text: str) -> int:
    #return len([char for char in text if char.isdigit()])

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestCountDigits(unittest.TestCase):
	def test_string_without_digits(self):
		self.assertEqual(
			count_digits('hi'),
			0
			)
            
	def test_digit_inside_word(self):
		self.assertEqual(
			count_digits('who is 1st here'),
			1
			) 
	
	def test_digit(self):
		self.assertEqual(
			count_digits('my numbers is 2'),
			1
			) 
	
	def test_digits(self):
		self.assertEqual(
			count_digits(
				"""This picture is an oil on canvas 
				painting by Danish artist Anna 
				Petersen between 1845 and 1910 year"""), 
				8
				)

		self.assertEqual(
			count_digits('5 plus 6 is'), 
			2
			)
	
	def test_empty_string(self):
		self.assertEqual(
			count_digits(''), 
			0
			) 


if __name__ == '__main__':
	unittest.main()

#a = count_digits('hi') #== 0
#b = count_digits('who is 1st here') #== 1
#c = count_digits('my numbers is 2') #== 1
#d = count_digits('This picture is an oil on canvas '
# 'painting by Danish artist Anna '
# 'Petersen between 1845 and 1910 year') #== 8
#e = count_digits('5 plus 6 is') #== 2
#f = count_digits('') #== 0	
#print(a, b, c, d, e, f, sep="\n")
