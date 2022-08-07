import unittest


#---------------------------------------------#
#               My Solution                   #
#---------------------------------------------#

def correct_sentence(text):
    text_list = list(text)
    text_list[0] = text_list[0].upper()
    if "." not in text_list[-1]:
        text_list.append(".")
    
    return ''.join(text_list)

#---------------------------------------------#
#             Better Solutions                #
#---------------------------------------------#

#def correct_sentence(text):
    #if not text.endswith('.'): text += '.'
    #return text[0].capitalize() + text[1:]

#def correct_sentence(text: str) -> str:   
    #return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

#---------------------------------------------#
#                   Tests                     #
#---------------------------------------------#

class TestCorrectSentence(unittest.TestCase):
    def test_nothing_to_correct(self):
        self.assertEqual(
            correct_sentence("Greetings, friends."), 
            "Greetings, friends."
        )
    
    def test_string_without_final_period(self):
        self.assertEqual(
            correct_sentence("Greetings, friends"), 
            "Greetings, friends."
        )
    
    def test_correct_sentence(self):
        self.assertEqual(
            correct_sentence("greetings, friends"), 
            "Greetings, friends."
        )

        self.assertEqual(
            correct_sentence("hi"), 
            "Hi."
        )

        self.assertEqual(
            correct_sentence("welcome to New York"), 
            "Welcome to New York."
        )


if __name__ == '__main__':
	unittest.main()
