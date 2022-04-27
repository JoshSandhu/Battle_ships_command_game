from random import randint

user = []
user_guesses = []
computer = []


def gen_board(board):
    """
    Creating a board of 5 "X" in 5 lists
    Arguments: Empty list
    Return: list with 5 lists of the letter X
    """
    for i in range(5):
        board.append(["X"] * 5)
    return board


