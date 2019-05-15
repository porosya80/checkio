#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run good-radix

# https://py.checkio.org/mission/good-radix/

# In mathematical numeral systems, the radix or base is the number of unique digits (including zero)    that a positional numeral system uses to represent numbers.    For example: in the decimal system, the radix is ten. This is because it has ten digits from 0 through 9.    In a system with a radix of 13, there would be 13 digits. For example:    a string of digits such as 398 denotes the decimal number3 * 13^2 + 9 * 13^1 + 8 * 13^0.    For the systems with a radix more than 10, we will use capital Latin symbols from A to Z, where A = 10, B = 11 ...
# 
# You are given some numbernwritten as a string with the radix equal tok (1 < k < 37).    We know that our number is divisible by(k - 1)without a remainder.    You should find the minimal possiblek, if it exists, or return 0.
# 
# For example: n = "18". As we can seekshould be greater than 8.
# If k == 9, then n = 17 in the decimal system and 17 % 8 == 1. The wrong radix.
# If k == 10, then n = 18 in the decimal system and 18 % 9 == 0. We found the answer.
# 
# 
# Input:A number as a string.
# 
# Output:The radix k as an integer.
# 
# How it is used:Let's familiarize with numeral systems more careful and examine the radix.    Many devices are built to accept numbers in decimal representation and display results in decimal. Often such devices convert from decimal to some internal radix on input, do all internal operations in that radix, and then convert the results from the internal radix to decimal on output. Such devices could in principle use any radix internally.    The people who design such computing devices sometimes wonder what would be the "best" radix to use internally -- radix economy.    The octal, hexadecimal and base-64 systems are often used in computing because of their ease as shorthand for binary.
# 
# Precondition:A number conforms regexp "[A-Z0-9]{1, 10}".
# 0 < number
# 
# 
# END_DESC

def checkio(number):
    """
    Your solution
    """
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("18") == 10, "Simple decimal"
    assert checkio("1010101011") == 2, "Any number is divisible by 1"
    assert checkio("222") == 3, "3rd test"
    assert checkio("A23B") == 14, "It's not a hex"
    assert checkio("IDDQD") == 0, "k is not exist"
    print('Local tests done')