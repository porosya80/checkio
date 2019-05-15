#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run morse-encoder

# https://py.checkio.org/mission/morse-encoder/

# Your task is to encrypt the text message using theMorse code. The input text will consist of letters (in uppercase and lowercase), numbers and whitespaces. There won't be any special characters ('&', '?', '#' etc.)
# You need to use 3 spaces between words and 1 space between each letter of each word.
# 
# 
# 
# Input:The secret message as a string.
# 
# Output:The same string, but encrypted.
# 
# Precondition:
# 0<len(text)<50
# Only English letters (in uppercase and lowercase), numbers and whitespaces.
# 
# 
# END_DESC

MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }

def morse_encoder(text):
    #replace this for solution
    return text

if __name__ == '__main__':
    print("Example:")
    print(morse_encoder('some text'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_encoder("some text") == "... --- -- .   - . -..- -"
    assert morse_encoder("2018") == "..--- ----- .---- ---.."
    assert morse_encoder("It was a good day") == ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"
    print("Coding complete? Click 'Check' to earn cool rewards!")