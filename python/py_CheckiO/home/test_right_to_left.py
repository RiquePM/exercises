import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def left_join(phrases):
	phrases = list(phrases)
	for i in phrases:
		if i == "right" or "right" in i:
			phrases[phrases.index(i)] = i.replace("right", "left")
	
	return ",".join(phrases)
				 
#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def left_join(phrases: tuple):
#	return ",".join(phrases).replace("right","left")

#left_join = lambda p:",".join(p).replace("right","left")

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestRightToLeft(unittest.TestCase):
	def test_right_to_left(self):
		self.assertEqual(
			left_join(("left", "right", "left", "stop")),
			"left,left,left,stop"
			)	 
    
	def test_right_to_left_inside_word(self):
		self.assertEqual(
			left_join(("bright aright", "ok")),
			"bleft aleft,ok"
			)
		
		self.assertEqual(
			left_join(("brightness wright",)),
			"bleftness wleft"
			) 
	
	def test_nothing_to_replace(self):
		self.assertEqual(
			left_join(("enough", "jokes")),
			"enough,jokes"
			) 


if __name__ == '__main__':
	unittest.main()
