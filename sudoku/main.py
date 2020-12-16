"""This module is where displaying of the board on CLI is taken care of"""

BOARD = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def display_board(bo):
    """Printing the sample board in a formatted way on CLI"""

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:   # end of 3 rows, print a straight line
            print("- - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):  # for each element in row
            if j % 3 == 0 and j != 0:   # end of 3 elements, print a straight line
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def empty_space(bo):
    """Finding the empty space to start our backtracking algorithm"""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j)  # row and column position of that element


return None
