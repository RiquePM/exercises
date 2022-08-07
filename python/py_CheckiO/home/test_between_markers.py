import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def between_markers(text, begin, end):
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

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def between_markers(text: str, begin: str, end: str) -> str:
    #start = text.find(begin) + len(begin) if begin in text else None
    #stop = text.find(end) if end in text else None
    #return text[start:stop]

#def between_markers(text: str, begin: str, end: str) -> str:
    #start, stop = map(text.find, (begin, end))
    #return text[(start + len(begin), 0)[start < 0]:(stop, None)[stop < 0]]

#def between_markers(text: str, begin: str, end: str) -> str:
    #if begin in text and end in text and text.index(begin) > text.index(end):
        #return ''
    #return text.split(begin)[-1].split(end)[0]    

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestBetweenMarkers(unittest.TestCase):
    def test_between_markers(self):
        self.assertEqual(between_markers(
            'What is >apple<', '>', '<'), 
            "apple"
            )	
        
        self.assertEqual(between_markers(
            "<head><title>My new site</title></head>", 
            "<title>", "</title>"), 
            "My new site"
            ) 
            
    def test_only_closing_marker(self):
        self.assertEqual(between_markers(
            'No[/b] hi', '[b]', '[/b]'), 
            'No'
            ) 
    
    def test_only_opening_marker(self):
        self.assertEqual(between_markers(
            'No [b]hi', '[b]', '[/b]'), 
            'hi'
            ) 
    
    def test_no_markers(self):
        self.assertEqual(between_markers(
            'No hi', '[b]', '[/b]'), 
            'No hi'
            )
    
    def test_markers_in_wrong_direction(self):
        self.assertEqual(between_markers(
            'No <hi>', '>', '<'), 
            ''
            ) 


if __name__ == '__main__':
	unittest.main()