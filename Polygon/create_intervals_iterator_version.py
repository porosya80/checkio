#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run create-intervals-iterator-version

# https://py.checkio.org/mission/create-intervals-iterator-version/

# From a set of ints (which will be an iterator of the sorted list) you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set. After that you have to create an iterator object which is linked to this list.
# 
# A closed interval includes its endpoints! The interval1..5, for example,  includes each valuexthat satisfies the condition1<= x<= 5.
# 
# Values can only be in the same interval if the difference between a value and the next  smaller value in the set equals one, otherwise a new interval begins. Of course, the  start value of an interval is excluded from this rule.
# A single value, that doesn’t fit into an existing interval becomes the start- and  endpoint of a new interval.
# 
# Input:An iterator of the sorted list of ints.
# 
# Output:An iterator object linked to the list of tuples.
# 
# 
# END_DESC

def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
                                                 (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
                                                 (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')