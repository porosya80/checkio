#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run rectangles-union

# https://py.checkio.org/mission/rectangles-union/

# Your mission is to calculate the area covered by a union of rectangles. The rectangles can have a non-empty intersection, which means that a simple sum of given rectangle areas doesn't work. Every rectangle is represented as 4 integers. The first two integers are the coordinates of a left-top corner, and the next two - of a bottom right corner.
# 
# 
# 
# 
# 
# Input:Iterable with tuples.
# 
# Output:Int.
# 
# 
# END_DESC

from typing import List, Tuple

def rectangles_union(recs: List[Tuple[int]]) -> int:
    # your code here
    return 0


if __name__ == '__main__':
    print("Example:")
    print(rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]) == 33
    assert rectangles_union([
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 19, 11),
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 16, 8)
    ]) == 0
    assert rectangles_union([
        
    ]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")