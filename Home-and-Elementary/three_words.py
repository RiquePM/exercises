#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def checkio(words: str):
	count = 0
	for word in words.split():
		if word.isalpha():
			count += 1
		else:
			count = 0
		
		if count == 3:
			return True
	
	return False 

#--------------------------------------------#
#	      Better Solutions	     	     #
#--------------------------------------------#

#import re
#def checkio(words):
    #return bool(re.search('\D+ \D+ \D+', words)) 
	#or 
	#return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))

#def checkio(x):
    #counter = 0
    #for e in x.split():
        #try: 
            #int(e)
            #counter = 0
        #except ValueError:
            #counter += 1
            #if counter >= 3: return True
    #return False


#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#
a = checkio("Hello World hello") #== True, "Hello"
b = checkio("He is 123 man") #== False, "123 man"
c = checkio("1 2 3 4") #== False, "Digits"
d = checkio("bla bla bla bla") #== True, "Bla Bla"
e = checkio("Hi") #== False, "Hi"
print(a, b, c, d, e, sep= "\n")
