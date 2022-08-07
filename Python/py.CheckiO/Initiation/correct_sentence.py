#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def correct_sentence(text: str) -> str:
    text_list = list(text)
    text_list[0] = text_list[0].upper()
    if "." not in text_list[-1]:
        text_list.append(".")
    
    return ''.join(text_list)

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#def correct_sentence(text):
    #if not text.endswith('.'): text += '.'
    #return text[0].capitalize() + text[1:]

#def correct_sentence(text: str) -> str:   
    #return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#

a = correct_sentence("greetings, friends") #== "Greetings, friends."
b = correct_sentence("Greetings, friends") #== "Greetings, friends."
c = correct_sentence("Greetings, friends.") #== "Greetings, friends."
d = correct_sentence("hi") #== "Hi."
e = correct_sentence("welcome to New York") #== "Welcome to New York."]
print(a, b, c, d, e, sep='\n')
