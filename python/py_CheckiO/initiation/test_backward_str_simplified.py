import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def backwards_string(val):
	val_list = list(val)
	c = list.reverse(val_list)
	rev_str = "".join(val_list)
	return rev_str

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def backward_string(val: str):
	#return val [::-1]

#backward_string = lambda val: val[::-1]

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBackwardString(unittest.TestCase):
	def test_backward_string(self):
		self.assertEqual(
			backwards_string("Henrique"),
			"euqirneH"
		)

if __name__ == '__main__':
	unittest.main()
