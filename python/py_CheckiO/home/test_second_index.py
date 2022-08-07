import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def second_index(text, symbol):
	for i in range(len(text)):
		if text[i] == symbol and i != text.index(symbol):
			return i
	return None		

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def second_index(text: str, symbol: str):
	#try:
        #return text.index(symbol, text.index(symbol) + 1)
    #except ValueError:
        #return None

#def second_index(text: str, symbol: str) -> [int, None]:
    #return None if text.count(symbol) < 2 else text.find(symbol, text.find(symbol) + 1)

#from contextlib import suppress
#def second_index(text: str, symbol: str):
	#with suppress(ValueError):
        #index1 = text.index(symbol)
        #return text.index(symbol, index1 + 1)

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestSecondIndex(unittest.TestCase):
    def test_second_index(self):
        self.assertEqual(
            second_index("sims", "s"),
            3
            )
        
        self.assertEqual(
            second_index("find the river", "e"),
            12
            )
        
        self.assertEqual(
            second_index("three occurrences", "r"),
            10
            )
        
        self.assertEqual(
            second_index("aaaaaa", "a"),
            1
            )
            
    def test_no_second_index(self):
        self.assertEqual(
            second_index("hi mayor", " "), 
            None
            )

    def test_blank_space_second_index(self):
        self.assertEqual(
            second_index("hi mr Mayor", " "),
            5
            )  


if __name__ == '__main__':
	unittest.main()
