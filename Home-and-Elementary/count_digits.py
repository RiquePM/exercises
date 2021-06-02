#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def count_digits(text:str):
	a = 0
	for i in text:
		if i.isdigit():
			a += 1
	return a	

#--------------------------------------------#
#			  Better Solutions			     #
#--------------------------------------------#

#def count_digits(text: str) -> int:
    #return sum(c.isdigit() for c in text)

#import re
#def count_digits(text):
    #return len(re.findall(r"\d", text))
    #return len(re.findall('[0-9]', text))

#def count_digits(text: str) -> int:
    #return len([char for char in text if char.isdigit()])

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = count_digits('hi') #== 0
b = count_digits('who is 1st here') #== 1
c = count_digits('my numbers is 2') #== 1
d = count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') #== 8
e = count_digits('5 plus 6 is') #== 2
f = count_digits('') #== 0	
print(a, b, c, d, e, f, sep="\n")