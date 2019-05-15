#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run bulls-and-cows

# https://py.checkio.org/mission/bulls-and-cows/

# In his grandfather's notebook Nicola found a description of an old game called"Bulls and Cows",    which was popular amongst ancient humans. He wants to try and play it with Stephan,    but Nicola does not losing games. That's where we come in!
# 
# The host thinks up a 4-digits sequence. The digits must all be different.    Then, in turn, you try to guess the sequence.    If the matching digits are on their right positions, they are called "bulls",    when they are on different positions, they are "cows". The host tells you how many "bulls" and "cows" you've guessed.    You should attempt to solve the code ineight turns(it is however, possible in seven turns).
# 
# On each step, your function receives a list with information from the previous steps.    Each element of the list contains your guess and the result in the following format"XXXX YBZC", where:
# 
# XXXX is a guessY is a quantity of "bulls"Z is a quantity of "cows"For each step your function returns your new guess as a string with four digits.
# 
# Let's consider an example. The hidden code is "5612". At the start your function receives an empty list.    Your guess is "1234" -- two digits are on different positions but appear in the code.    So the next call will be ["1234 0B2C"]. Your next guess is "6512" -- two "bulls", two "cows".    The next input is ["1234 0B2C", "6512 2B2C"]. And the last guess is "5612". Aaand you win!
# 
# Input:Information from your last steps as a list of strings.
# 
# Output:The guess as a string.
# 
# Precondition:Step information satisfies regexp "[0-9]{4} [0-4]B[0-4]C"
# 
# 
# 
# END_DESC

def checkio(data):
    #your function
    return "0123"

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, goal):
        recent = []
        for step in range(8):
            user_result = func(recent)
            bulls = cows = 0
            for u, g in zip(user_result, goal):
                if u == g:
                    bulls += 1
                elif u in goal:
                    cows += 1
            recent.append("{0} {1}B{2}C".format(user_result, bulls, cows))
            if bulls == 4:
                print("{0} Win with {1} steps.".format(goal, step + 1))
                return True
        print("{0} Fail.".format(goal))
        return False

    assert check_solution(checkio, "1234"), "1234"
    assert check_solution(checkio, "6130"), "6130"
    assert check_solution(checkio, "0317"), "0317"
    assert check_solution(checkio, "9876"), "9876"