#--------------------------------------------#
#				 My Solution 				 #
#--------------------------------------------#
def split_pairs(a):
	if len(a) % 2 == 0:
		pairs = [a[i] + a[i+1] for i in range(0, len(a), 2)]
		
	else:
		b = a + '_'
		pairs = [b[i] + b[i+1] for i in range(0, len(b), 2)]
	
	return pairs

#--------------------------------------------#
#			   Better Solutions			     #
#--------------------------------------------#

#def split_pairs(a):
	#return [(a + '_')[i:i+2] for i in range(0, len(text), 2)]

#def split_pairs(a):
	#if len(a) % 2 != 0:
		#a = a + '_'
	#return [a[i:i + 2] for i in range(0, len(a), 2)]	

#from textwrap import wrap → olhar a biblioteca texwrap
#def split_pairs(a):
	#a = a + '_' if len(a) % 2 else a
	#return wrap(a, 2)

#import itertools, operator → olhar a biblioteca itertools
#def split_pairs(a):
	#it = itertools.chain(a, '_')
	#return map(operator.add, it, it) → olhar a função map

#def split_pairs(a):
	#return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')] → olhar a função zip 

#def split_pairs(a):
	#return [a[i-1]+c for i,c in enumerate(a+'_'*(len(a)%2)) if i%2] → olhar a função enumerate

#split_pairs = lambda a: [x + y for x, y in zip(a[::2], a[1::2] + '_')]

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = split_pairs("abcd")
b = split_pairs("abc")
c = split_pairs("")
d = split_pairs("a")
print(a, b, c, d, sep = '\n')
		

