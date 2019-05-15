#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run triangle-angles

# https://py.checkio.org/mission/triangle-angles/

# You are given the lengths for each side on a triangle.    You need to find all three angles for this triangle.    If the given side lengths cannot form a triangle (or form a degenerated triangle),    then you must return all angles as 0 (zero).    The angles should be represented as a list of integers inascending order.    Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
# 
# 
# 
# Input:The lengths of the sides of a triangle as integers.
# 
# Output:Angles of a triangle in degrees as sorted list of integers.
# 
# Precondition:
# 0 < a,b,c ≤ 1000
# 
# 
# END_DESC

from typing import List
from math import acos
from math import degrees

def checkio(a: int, b: int, c: int) -> List[int]:


    if a + b > c and a + c > b and b + c > a:
        ang_ab = acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))
        ang_bc = acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))
        ang_ac = acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))

        return sorted(round(degrees(i)) for i in (ang_ab, ang_bc, ang_ac))

    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")