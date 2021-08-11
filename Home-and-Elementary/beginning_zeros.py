#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def beginning_zeros(number: str):
    num = number.lstrip('0')
    return (len(number) - len(num))

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#
#def beginning_zeros(number: str) -> int:
    #return len(number) - len(number.lstrip('0'))

#import re
#def beginning_zeros(number: str) -> int:
    #return len(re.sub(r'[^0].*$', '', number)) 


#--------------------------------------------#
#					Test					 #
#--------------------------------------------#
a = beginning_zeros('100') #== 0
b = beginning_zeros('001') #== 2
c = beginning_zeros('100100') #== 0
d = beginning_zeros('001001') #== 2
e = beginning_zeros('012345679') #== 1
f = beginning_zeros('0000') #== 4
print(a, b, c, d, e, f, sep='\n')