#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run three-points-circle

# https://py.checkio.org/mission/three-points-circle/

# Nicola discovered a calliper inside a set of drafting tools he received as a gift.    Seeing the caliper, he has decided to learn how to use it.
# 
# Through any three points that do not exist on the same line, there lies a unique circle.    The points of this circle are represented in a string with the coordinates like so:
# 
# 
#     "(x1,y1),(x2,y2),(x3,y3)"
# 
# Wherex1,y1,x2,y2,x3,y3are digits.
# 
# You should find the circle for three given points, such    that the circle lies through these point and return the result as a string    with the equation of the circle.    In a Cartesian coordinate system (with an X and Y axis),    the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:
# 
# 
#     "(x-x0)^2+(y-y0)^2=r^2"
# 
# wherex0,y0,rare decimal numbers rounded totwo decimal points.    Remove extraneous zeros and all decimal points, they are not necessary.    For rounding, use the standard mathematical rules.
# 
# 
# 
# Input:Coordinates as a string..
# 
# Output:The equation of the circle as a string.
# 
# Precondition:All three given points do not lie on one line.
# 0 < xi, yi, r < 10
# 
# 
# END_DESC

import math
def zero(number):
    number = round(number, 2)
    if number - int(number) == 0:
        result = (str(number).split(".")[0])
    else:
        result = number
    return result

def checkio(data):
    data = data.split("),")
    x1 = int(data[0][1])
    y1 = int(data[0][3])
    x2 = int(data[1][1])
    y2 = int(data[1][3])
    x3 = int(data[2][1])
    y3 = int(data[2][3])

    x0 = -(1 / 2) * (y1 * (x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2) + y2 * (-x1 ** 2 + x3 ** 2 - y1 ** 2 + y3 ** 2) + y3 * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2)) / (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    y0 = (1 / 2) * (x1 * (x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2) + x2 * (-x1 ** 2 + x3 ** 2 - y1 ** 2 + y3 ** 2) + x3 * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2)) / (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    r = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # print (x0,y0,r)
    # print(zero(x0), zero(y0), zero(r))
    # print("(x-{0})^2+(y-{1})^2={2}^2".format(zero(x0), zero(y0), zero(r)))
    return ("(x-{0})^2+(y-{1})^2={2}^2".format(zero(x0), zero(y0), zero(r)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    # checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    # checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    checkio("(1,1),(2,1),(1,2)")