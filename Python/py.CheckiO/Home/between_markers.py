#--------------------------------------------#
#		My Solution		     #
#--------------------------------------------#
def between_markers(text: str, begin: str, end: str):
    if begin in text and end in text:
        if text.find(begin)>text.find(end):
            return ""
        else:
            return text[text.find(begin)+len(begin):text.find(end)]
    elif begin not in text and end not in text:
        return text[:]
    elif begin not in text:
        return text[:text.find(end)]
    elif end not in text:
        return text[text.find(begin)+len(begin):]

#--------------------------------------------#
#	      Other Solutions	     	     #
#--------------------------------------------#

#def between_markers(text: str, begin: str, end: str) -> str:
    #start = text.find(begin) + len(begin) if begin in text else None
    #stop = text.find(end) if end in text else None
    #return text[start:stop]

#def between_markers(text: str, begin: str, end: str) -> str:
    #start, stop = map(text.find, (begin, end))
    #return text[(start + len(begin), 0)[start < 0]:(stop, None)[stop < 0]] → if-tuple slicing

#def between_markers(text: str, begin: str, end: str) -> str:
    #if begin in text and end in text and text.index(begin) > text.index(end):
        #return ''
    #return text.split(begin)[-1].split(end)[0]    

#--------------------------------------------#
#		    Test		     #
#--------------------------------------------#
a = between_markers('What is >apple<', '>', '<') #== "apple", "One sym"
b = between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") #== "My new site", "HTML"
c = between_markers('No[/b] hi', '[b]', '[/b]') #== 'No', 'No opened'
d = between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
e = between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
f = between_markers('No <hi>', '>', '<') #== '', 'Wrong direction'
print(a, b, c, d, e, f, sep="\n")
