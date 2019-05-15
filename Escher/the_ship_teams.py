#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py check the-ship-teams

# https://py.checkio.org/mission/the-ship-teams/

#
# END_DESC


def two_teams(sailors: dict):

    ship1, ship2 = [], []
    for sail, age in sailors.items():
        if 20 <= age <= 40:
            ship2.append(sail)
        else:
            ship1.append(sail)
    return [
        sorted(ship1),
        sorted(ship2)
    ]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'],
            ['Smith', 'Wesson']
    ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'],
            ['Johnson']
    ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
