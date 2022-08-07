import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def max_digit(number): 
	return int(max(str(number)))

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#max_digit = lambda number: int(max(str(number)))

#--------Simple explanation of lambda functions--------#
						
#def name(whatever arguments): --> lambda whatever arguments: some expression
#                                                                 |     
    #return some expression --------------------------------------


#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestMaxDigit(unittest.TestCase):
	def test_max_digit(self):
		self.assertEqual(
            max_digit(52), 
            5
        )

if __name__ == '__main__':
	unittest.main()

