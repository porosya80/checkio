#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run long-non-repeat

# https://py.checkio.org/mission/long-non-repeat/

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".
# 
# Input:String.Output:String.
# 
# 
# END_DESC

def non_repeat(line):
    substring = ""
    temp_sub = ""
    for ch in line:
        if ch not in temp_sub:
            temp_sub += ch
            # print(temp_sub)
        else:
            if len(substring) < len(temp_sub):
                substring = temp_sub
            temp_sub = temp_sub[temp_sub.index(ch)+1:]+ch
            # print(substring)

    return substring if len(substring) >= len(temp_sub) else temp_sub





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')