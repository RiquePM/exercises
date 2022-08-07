#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def first_word(text:str):
	text = text.replace(".", " ").replace(",", " ")
	return text.split()[0]

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#import re
#def first_word(text: str) -> str:
    #return re.search("([\w']+)", text).group(1) or return re.search("[a-zA-Z']+", text).group()

#def first_word(text: str) -> str:
    #return text.replace(',', ' ').replace('.', ' ').split(maxsplit=1)[0] -> Use of maxsplit

#import re
#word = re.compile(r"[\w']+")
#first_word = lambda text: word.search(text).group()

#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#
a = first_word("Hello world") #== "Hello"
b = first_word(" a word ") #== "a"
c = first_word("don't touch it") #== "don't"
d = first_word("greetings, friends") #== "greetings"
e = first_word("... and so on ...") #== "and"
f = first_word("hi") #== "hi"
g = first_word("Hello.World") #== "Hello"
print(a, b, c, d, e, f, g, sep="\n")
