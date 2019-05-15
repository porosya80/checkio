#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run first-word

# https://py.checkio.org/mission/first-word/

# You are given a string where you have to find its first word.
# 
# When solving a task pay attention to the following points:
# 
# There can be dots and commas in a string.A string can start with a letter or, for example, a dot or space.A word can contain an apostrophe and it's a part of a word.The whole text can be represented with one word and that's it.Input:A string.
# 
# Output:A string.
# 
# Precondition:the text can contain a-z A-Z , . '
# 
# 
# END_DESC

def first_word(text: str) -> str:
    text= text.replace(',', " ").replace('.', ' ')
    text = text.split()
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")