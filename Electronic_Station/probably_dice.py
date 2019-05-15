#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run probably-dice

# https://py.checkio.org/mission/probably-dice/

# You're on your way to a board game convention.    Chances are there’ll be some stiff competition,    so you decide to learn more about dice probabilities since you suspect you'll be rolling a lot of them soon.
# 
# Typically, when using multiple dice, you simply roll them and sum up all the result.    To get started with your investigation of dice probability, write a function that takes the number of dice,    the number of sides per die and a target number and    returns the probability of getting a total roll of exactly the target value.    The result should be given with four digits precision as ±0.0001.    For example, if you roll 2 six-sided dice, the probability of getting exactly a 3 is 2/36 or 5.56%,    which you should return as ≈0.0556.
# 
# 
# 
# For each test, assume all the dice are the same and are numbered from 1 to the number of sides, inclusive.    So a 4-sided die (D4)  would have an equal chance of rolling a 1, 2, 3 or 4.    A 20-sided die (D20) would have an equal chance of rolling any number from 1 to 20.
# 
# Tips:Be careful if you want to use a brute-force solution -- you could have a very, very long wait for edge cases.
# 
# Input:Three arguments. The number of dice, the number of sides per die and the target number as integers.
# 
# Output:The probability of getting exactly target number on a single roll of the given dice as a float.
# 
# Example:
# 
# 
# probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
# probability(2, 6, 4) == 0.0833
# probability(2, 6, 7) == 0.1667
# probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
# probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
# probability(3, 6, 7) == 0.0694
# probability(10, 10, 50) == 0.0375
# Preconditions:
# 1 ≤dice_number≤ 10
# 2 ≤sides≤ 20
# 0 ≤target< 1000
# 
# 
# END_DESC

def probability(dice_number, sides, target):
    base_per = round(1/(sides),4)
    sides_table = [[base_per for n in range(sides)] for k in range((sides*(dice_number))+1)]
    ishod = dict.fromkeys(range(sides*(dice_number)+1), 0)
    for dice in range(1,dice_number):

        for i in range(1,(sides*(dice))):
            for k in range(1, sides):
                # print(k)
                sides_table[i][k] = round(sides_table[i][k] * base_per,4)
                ishod[i+k] += sides_table[i][k]




    print('\n'.join([' '.join(['{:4}'.format(item) for item in row]) for row in sides_table]))
    # for i in range(1, sides+1):
    #     for k in range(1, sides+1):
    #             ishod[i+k] += 1
    # for key in ishod:
    #     ishod[key] = round(ishod[key] * base_per**2,4)
    #
    # if dice_number > 2:
    #     for dice in range(2,dice_number+1):
    #         for i in range(1, sides * dice+1):
    #             for k in range(1, sides + 1):
    #                 ishod[i + k] += ishod[i + k] +




    print(ishod.items())
    print(base_per)
    
    
    # print(ishod[target])
    return 0.0

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    # assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    # assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
    probability(2, 6, 3)