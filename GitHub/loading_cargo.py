#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run loading-cargo

# https://py.checkio.org/mission/loading-cargo/

# "Look Stephen, here's a list of the items that need to be loaded onto the ship. We're going to need a lot of        batteries." Nikola handed him a notepad.
# 
# "What are the numbers next to the items?"
# 
# "That is the weight of each item."
# 
# "Er, why?"
# 
# "So you can see how much your trading cards and comic book collection will weigh us down during flight." Rang        Sofias voice from the phone tube.
# 
# "What is she talking about?” asked Nikola “Ooooh, nevermind, that was sarcasm. It’s important because your        load-stabilizing belt is broken and there is no way that we can find a new one right now. That’s why, when you        carry the things on the list, you’ll have to redistribute their weights in order to get the minimal weight in        each arm."
# 
# "Okay, so I have to figure out how many batteries I should hold in each hand to prevent them from breaking when        they inevitably fall to the ground. Got it."
# 
# You have been given a list of integer weights.    You should help Stephen distribute these weights into two sets,    such that the difference between the total weight of each set is as low as possible.
# 
# Input data:A list of the weights as a list of integers.
# 
# Output data:The number representing the lowest possible weight difference as a positive integer.
# 
# Precondition:
# 0 < len(weights) ≤ 10
# all(0 < x < 100 for x in weights)
# 
# 
# END_DESC

def checkio(data):

    #replace this for solution
    return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"