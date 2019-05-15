#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run group-equal-consecutive

# https://py.checkio.org/mission/group-equal-consecutive/

# Given a list of elements, create and return a list whose elements are lists that contain the consecutive runs of equal elements of the original list. Note that elements that aren’t duplicated in the original list should become singleton lists in the result, so that every element gets included in the resulting list of lists.
# 
# Input:List of str and int.
# 
# Output:List of lists of str and int
# 
# The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

def group_equal(els):
    # your code here
    return els


if __name__ == '__main__':
    print("Example:")
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1,1],[4,4,4],["hello","hello"],[4]]
    assert group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]]
    assert group_equal([1]) == [[1]]
    assert group_equal([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")