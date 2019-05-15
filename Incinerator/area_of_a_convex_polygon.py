#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run area-of-a-convex-polygon

# https://py.checkio.org/mission/area-of-a-convex-polygon/

# There is a convex polygon on a coordinate plane. This polygon is presented as a list of vertices coordinates.    Each vertex is connected sequentially with the last connecting back to the first.    A polygon hasNvertices.    You should write a program that will calculate the area of a polygon.    The result should be given with one digits precision as ±0.1.
# 
# 
# 
# Input:Coordinates as a list of lists. Each list contains two integers.
# 
# Output:The area of the polygon as a float.
# 
# Precondition:3 ≤ N ≤ 8
# ∀ x, y ∈ coordinates : 0 ≤ x ≤ 10; 0 ≤ y ≤ 10;
# 
# 
# 
# END_DESC

def checkio(data):
    res_tmp = 0
    data.append(data[0])
    for i in range(len(data)-1):
        res_tmp += ((data[i][0] * data[i+1][1]) - (data[i][1] * data[i+1][0]))
    return abs(res_tmp / 2)

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"