#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def backward_str_by_word(text:str):
	txt_list = [word[::-1] for word in text.split(" ")]
	return " ".join(txt_list)

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#return " ".join(word[::-1] for word in text.split(" "))

#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#

a = backward_str_by_word('') #== ''
b = backward_str_by_word('world') #== 'dlrow'
c = backward_str_by_word('hello world') #== 'olleh dlrow'
d = backward_str_by_word('hello   world') #== 'olleh   dlrow'
e = backward_str_by_word('welcome to a game') #== 'emoclew ot a emag'		

print(a, b, c, d, e, sep="\n")
