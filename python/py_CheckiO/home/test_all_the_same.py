import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def all_the_same(elements):
	for i in range(len(elements)):
		if elements[i] != elements[i-1]:
			return False
	return True
 
#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def all_the_same(elements):
#	return elements[1:] == elements[:-1]

#def all_the_same(elements):
#	return len(set(elements)) <= 1

#def all_the_same(elements):
    #return all(elements[0] == e for e in elements[1:])

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestAllSame(unittest.TestCase):
	def test_all_the_same_int(self):
		self.assertTrue(all_the_same([1, 1, 1]))
	
	def test_not_all_the_same(self):
		self.assertFalse(all_the_same([1, 2, 1]))
	
	def test_all_the_same_string(self):
		self.assertTrue(all_the_same(['a', 'a', 'a']))
	
	def test_all_the_same_empty_seq(self):
		self.assertTrue(all_the_same([]))
	
	def test_all_the_same_one_elem(self):
		self.assertTrue(all_the_same([1]))


if __name__ == '__main__':
	unittest.main()