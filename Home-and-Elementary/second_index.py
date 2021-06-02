#--------------------------------------------#
#				My Solution 				 #
#--------------------------------------------#
def second_index(text:str, symbol: str):
	for i in range(len(text)):
		if text[i] == symbol and i != text.index(symbol):
			return i
	return None		

#--------------------------------------------#
#			  Better Solutions				 #
#--------------------------------------------#

#def second_index(text: str, symbol: str):
	#try:
        #return text.index(symbol, text.index(symbol) + 1)
    #except ValueError:
        #return None

#def second_index(text: str, symbol: str) -> [int, None]:
    #return None if text.count(symbol) < 2 else text.find(symbol, text.find(symbol) + 1)

#from contextlib import suppress
#def second_index(text: str, symbol: str):
	#with suppress(ValueError):
        #index1 = text.index(symbol)
        #return text.index(symbol, index1 + 1)

#--------------------------------------------#
#					Test					 #
#--------------------------------------------#

a = second_index("sims", "s") #== 3
b = second_index("find the river", "e") #== 12
c = second_index("hi", " ") #is None
d = second_index("hi mayor", " ") #is None
e = second_index("hi mr Mayor", " ") #== 5
f = second_index("three occurrences", "r") #== 10
g = second_index("aaaaaa", "a")
print(a, b, c, d, e, f, g, sep='\n')