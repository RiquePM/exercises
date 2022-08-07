import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def first_word(text):
	text = text.replace(".", " ").replace(",", " ")
	return text.split()[0]

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#import re
#def first_word(text: str) -> str:
    #return re.search("([\w']+)", text).group(1) or return re.search("[a-zA-Z']+", text).group()

#def first_word(text: str) -> str:
    #return text.replace(',', ' ').replace('.', ' ').split(maxsplit=1)[0] -> Use of maxsplit

#import re
#word = re.compile(r"[\w']+")
#first_word = lambda text: word.search(text).group()

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBetweenMarkers(unittest.TestCase):
    def test_first_word(self):
        self.assertEqual(
            first_word("Hello world"), 
            "Hello"
        )	
        
        self.assertEqual(
            first_word("don't touch it"), 
            "don't"
        )

        self.assertEqual(
            first_word("greetings, friends"), 
            "greetings"
        )

        self.assertEqual(
            first_word("hi"), 
            "hi"
        )

        self.assertEqual(
            first_word("Hello.World"), 
            "Hello"
        ) 
            
    def test_string_starting_with_blank_space(self):
        self.assertEqual(
            first_word(" a word "), 
            "a"
        ) 
    
    def test_string_starting_with_ellipsis(self):
        self.assertEqual(
            first_word("... and so on ..."), 
            "and"
        ) 


if __name__ == '__main__':
	unittest.main()
