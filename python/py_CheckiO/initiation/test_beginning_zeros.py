import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def beginning_zeros(number):
    num = number.lstrip('0')
    return (len(number) - len(num))

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def beginning_zeros(number: str) -> int:
    #return len(number) - len(number.lstrip('0'))

#import re
#def beginning_zeros(number: str) -> int:
    #return len(re.sub(r'[^0].*$', '', number)) 


#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBeginningZeros(unittest.TestCase):
    def test_not_beginning_with_zero(self):
        self.assertEqual(
            beginning_zeros('100'), 
            0
        )
        
        self.assertEqual(
            beginning_zeros('100100'), 
            0
        )
    
    def test_beginning_with_zero(self):
        self.assertEqual(
            beginning_zeros('001'), 
            2
        )
        
        self.assertEqual(
            beginning_zeros('001001'), 
            2
        )

        self.assertEqual(
            beginning_zeros('012345679'), 
            1
        )

        self.assertEqual(
            beginning_zeros('0000'), 
            4
        )


if __name__ == '__main__':
	unittest.main()
