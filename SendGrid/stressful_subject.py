#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run stressful-subject

# https://py.checkio.org/mission/stressful-subject/

# 
# END_DESC

def is_stressful(subj):
    ALPHABET = list(map(chr, range(97, 123)))
    if subj.isupper() or subj[-1:-4:-1] == "!!!":
        return True
    words = ['help', 'asap', 'urgent']
    subj = subj.lower()
    result = subj[0]

    for i in range(1, len(subj)):
        if subj[i] in ALPHABET and subj[i] != subj[i-1]:
            result += subj[i]

    for word in words:
        if word in result:
            return True
    
    return False
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')