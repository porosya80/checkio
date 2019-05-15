#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run bacteria-colonies

# https://py.checkio.org/mission/bacteria-colonies/

# Biologists use bacteria to clone DNA for sequencing. These bacteria are then injected with the DNA that needs to be    cloned and allowed to reproduce on a large plate. As these bacteria reproduce, they begin to form colonies. Only    bacteria from healthy colonies will be used for sequencing. And here bioinformatics take the game and use    technologies to automate these process.
# 
# Let's represent a plate snapshot as a pixel grid. You are given this grid as a binary matrix where 1 is bacteria    cell and 0 is empty. Our goal is find the largest healthy bacteria colony which has grown uniformly. Bacteria can    grow in four adjacent cells and bacteria colony is a set of bacterias that are connected. The healthy colonies look    similar to the images represented below.
# 
# 
# 
# Next, we can see that unhealthy colonies are marked with an orange color. Remember that a single cell is not a    colony, so it cannot be counted as healthy colony.
# 
# 
# 
# Your mission is to find the largest healthy colony and return the coordinates of the center cell. The top-left cell    has coordinates (0, 0). If on the plate no a healthy colony, then return (0, 0) (or [0, 0]). If on the plate several    largest colonies with the same size, then return any of them.
# 
# Input:A grid as a tuple of tuples with integers 1/0.
# 
# Output:The coordinates of the largest colony as a list or a tuple of two integers.
# 
# 
# Precondition:
# 5 ≤ len(grid) ≤ 20
# all(5 ≤ len(row) ≤ 20 for row in grid)
# 
# 
# END_DESC

def healthy(grid):
    return 0, 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        return list(result) in answers

    check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])