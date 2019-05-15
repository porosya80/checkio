#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run chess-knight

# https://py.checkio.org/mission/chess-knight/

# Your friend loves chess very much, but he's not a strong player. You can help him by using your programming skills.
# If this mission is too simple for you, try another one from this set -The shortest Knight's path.
# 
# Your task is to write a function that can find all of the chessboard cells to which the Knight can move. The input data will consist of a start cell and the amount of moves that the Knight will make. There is only one figure on the board - your Knight.
# If the same cell appears more than once - do not add it again.You should return the list of all of the possible cells and sort them as follows:in alphabetical order (from 'a' to 'h') and in ascending order (from 'a1' to 'a8' and so on).
# 
# 
# 
# Input:A start cell, the number of moves.
# 
# Output:A list of all of the possible cells.
# 
# Precondition:
# 1<= the number of moves<= 2
# 
# 
# 
# END_DESC

def look_neib(coords):
    xs, ys = coords
    result = []
    MOVES = ((2, 1),
             (2, -1),
             (1, -2),
             (-1, -2),
             (-2, 1),
             (-2, -1),
             (1, 2),
             (-1, 2))

    for x, y in MOVES:
        if 0 < xs+x <= 8 and 0 < ys+y <= 8:
            result.append((xs+x, ys+y))

    return result


def chess_knight(start, moves):
    result = set()
    letters = 'abcdefgh'
    coords = letters.index(start[0])+1, int(start[1])
    queue = look_neib(coords)
    result.update(queue)
    # print(result)
    # print(queue)
    if moves == 2:
        while queue:
            # print(look_neib(queue2.pop()))
            result.update(look_neib(queue.pop()))
    result = [str(letters[x-1])+str(y) for x, y in result]
    return sorted(result)
if __name__ == '__main__':
    print("Example:")
    print(chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")