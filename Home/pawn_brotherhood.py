#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

def safe_pawns(pawns):
    CONV_TABLE = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    chess_board = [["." for x in range(8)]for y in range(8)]
    result = 0
    for pawn in pawns:
        chess_board[-(int(pawn[-1]))][CONV_TABLE.get(pawn[0])] = "X"

    for row, chess_row in enumerate(chess_board):
        for column, place in enumerate(chess_row):
            if place == "X":
                if row != 7:
                    if column != 0 and column != 7:
                        if chess_board[row+1][column-1] == "X" or chess_board[row+1][column+1] == "X":
                            result += 1
                    elif column == 0:
                        if chess_board[row+1][column+1] == "X":
                            result += 1
                    elif column == 7:
                        if chess_board[row+1][column-1] == "X":
                            result += 1







    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    # safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    safe_pawns(["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"])