#--------------------------------------------#
#                My Solution                 #
#--------------------------------------------#
def popular_words(text:str, words: list):
	text = text.lower().split()
	return {word: text.count(word) for word in words}

#--------------------------------------------#
#             Better Solutions               #
#--------------------------------------------#

#def popular_words(text, words):
	#return dict(zip(words, map(tex.lower().split().count, words)))

#--------------------------------------------#
#                   Test                     #
#--------------------------------------------#

a = popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) #== {
        #'i': 4,
        #'was': 3,
        #'three': 0,
        #'near': 0
    #}	
print(a)    