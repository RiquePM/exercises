import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def end_zeros(num):
	num_str = str(num)
	count = 0
	for i in num_str[::-1] :
		if i == "0":
			count += 1
		else:
			break
	return count

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def end_zeros(num: int) -> int:
    #s = str(num)
    #return len(s) - len(s.rstrip('0'))

#def end_zeros(number):
    #import re
    #return len(re.search('0*$', str(number)).group(0))

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestEndZeros(unittest.TestCase):
	def test_end_zeros(self):
		self.assertEqual(
			end_zeros(0), 
			1
		)

		self.assertEqual(
			end_zeros(10), 
			1
		)

		self.assertEqual(
			end_zeros(100100), 
			2
		)
	
	def test_not_end_zeros(self):
		self.assertEqual(
			end_zeros(1), 
			0
		)

		self.assertEqual(
			end_zeros(101), 
			0
		)

		self.assertEqual(
			end_zeros(245), 
			0
		)

if __name__ == '__main__':
	unittest.main()
