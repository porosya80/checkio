#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run correct-sentence

# https://py.checkio.org/mission/correct-sentence/

# For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
#
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
#
# Input:A string.
#
# Output:A string.
#
# Precondition:No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
#
#
# END_DESC


def correct_sentence(text: str) -> str:
    text = text[0].upper()+text[1:]
    if text[-1] != '.':
        text += '.'

    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
