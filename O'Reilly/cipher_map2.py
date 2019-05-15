#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run cipher-map2

# https://py.checkio.org/mission/cipher-map2/

# 
# END_DESC

def recall_password(cipher_grille, ciphered_password):
    result = []
    for trys in range(len(cipher_grille)):
        for row in range(len(cipher_grille)):
            # print (row)
            for column in range(len(cipher_grille[row])):
                if cipher_grille[row][column] == "X":
                   result += ciphered_password[row][column]
        cipher_grille = list(zip(*cipher_grille[::-1]))
    
    return "".join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'