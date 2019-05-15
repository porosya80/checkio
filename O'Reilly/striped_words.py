#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run striped-words

# https://py.checkio.org/mission/striped-words/

# Our robots are always working to improve their linguistic skills.    For this mission, they research the latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.     These words are separated by white-spaces and punctuation marks.    Numbers are not considered words in this mission (a mix of letters and digits is not a word either).    You should count the number of words (striped words) where the vowels with consonants are alternating,    that is; words that you count cannot have two consecutive vowels or consonants.    The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCT = " ,."


def checkio(text):
    result = 0
    cnt = 0
    text = [word for word in (text.replace(' ', ',').replace(".",",").upper()).split(",") if not len(word) <= 1 or
            any([False for char in word if char.isdigit()])]
    for word in text:
        for count , char in enumerate(word[1:], 1):
            if char in VOWELS:
                if word[count-1] in CONSONANTS:
                    cnt += 1
                else:
                    cnt = 0
                    break
            elif char in CONSONANTS:
                if word[count - 1] in VOWELS:
                    cnt += 1
                else:
                    cnt = 0
                    break
        if cnt >= 1:
            result += 1
        cnt = 0
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"