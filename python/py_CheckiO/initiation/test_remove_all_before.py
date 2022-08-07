import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def remove_all_before(items, border):
	if border in items:
		for i in range(len(items)):
			if items[i] == border:
				return items[i:]	
	return items

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def remove_all_before(items: list, border: int):
	#return items[items.index(border):] if border in items else items		
	
#exception handling solution
#try:
	#return items[items.index(border):]
#except ValueError:
	#return items	

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestRemoveAllBefore(unittest.TestCase):
	def test_remove_all_before(self):
		self.assertEqual(
			remove_all_before([1, 2, 3, 4, 5, 6, 7, 8], 4),
			[4, 5, 6, 7, 8]
		)

		self.assertEqual(
			remove_all_before([1, 1, 2, 2, 3, 3], 2),
			[2, 2, 3, 3]
		)
	
	def test_empty_list(self):
		self.assertEqual(
			remove_all_before([], 3),
			[]
		)
	
	def test_target_bigger_than_the_biggest_in_list(self):
		self.assertEqual(
			remove_all_before([1, 2, 3, 4, 5, 6, 7, 8], 9),
			[1, 2, 3, 4, 5, 6, 7, 8]
		)
	
	def test_list_with_values_equal_to_target(self):
		self.assertEqual(
			remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7),
			[7, 7, 7, 7, 7, 7, 7, 7, 7]
		)

if __name__ == '__main__':
	unittest.main()

