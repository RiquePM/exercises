import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def three_words(words):
	count = 0
	for word in words.split():
		if word.isalpha():
			count += 1
		else:
			count = 0
		
		if count == 3:
			return True
	
	return False 

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#import re
#def checkio(words):
    #return bool(re.search('\D+ \D+ \D+', words)) 
	#or 
	#return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))

#def checkio(x):
    #counter = 0
    #for e in x.split():
        #try: 
            #int(e)
            #counter = 0
        #except ValueError:
            #counter += 1
            #if counter >= 3: return True
    #return False


#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestThreeWords(unittest.TestCase):
	def test_three_words(self):
		self.assertTrue(
			three_words("Hello World hello"),
			)
		self.assertTrue(
			three_words("bla bla bla bla"),
			)
	
	def test_not_three_words(self):
		self.assertFalse(
			three_words("He is 123 man"),
			) 
	
	def test_digits(self):
		self.assertFalse(
			three_words("1 2 3 4"),
			) 
	
	def test_single_word(self):
		self.assertFalse(
			three_words("Hi"), 
			) 


if __name__ == '__main__':
	unittest.main()
