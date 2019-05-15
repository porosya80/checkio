#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run the-square-chest

# https://py.checkio.org/mission/the-square-chest/

# On the chest keypad is a grid of numbered dots.    The grid is comprised of a square shaped array of dots and contains lines    that connect some pairs of adjacent dots.    The answer to the code is the number of squares that are formed by these lines.    For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.
# 
# 
# 
# The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented by lists of two numbers.
# 
# Input:A list of lines as a list of list. Each list consists of the two integers.Output:The quantity of squares formed as an integer.
# END_DESC

from typing import List

def checkio(lines_list: List[List[int]]) -> int:
    """Return the quantity of squares"""
    return 0


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    print("Coding complete? Click 'Check' to earn cool rewards!")