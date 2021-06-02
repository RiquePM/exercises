#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def left_join(phrases: tuple):
	phrases = list(phrases)
	for i in phrases:
		if i == "right" or "right" in i:
			phrases[phrases.index(i)] = i.replace("right", "left")
	
	return ",".join(phrases)
				 
#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#

#def left_join(phrases: tuple):
#	return ",".join(phrases).replace("right","left")

#left_join = lambda p:",".join(p).replace("right","left")

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = left_join(("left", "right", "left", "stop")) #== "left,left,left,stop", "All to left"
b = left_join(("bright aright", "ok")) #== "bleft aleft,ok", "Bright Left"
c = left_join(("brightness wright",)) #== "bleftness wleft", "One phrase"
d = left_join(("enough", "jokes")) #== "enough,jokes", "Nothing to replace"
print(a, b, c, d, sep = '\n')