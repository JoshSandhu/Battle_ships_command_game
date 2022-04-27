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


def print_board(board):
    """
    Prints the board list of X,
    Replacing the lists formatting with spaces
    Argument: List
    """
    for ind in board:
        print(" ".join(ind))


def random_num(board):
    """
    Generate the random number between 0 and the length of the board(Minus one)
    Argument: List
    """
    return randint(0, len(board) - 1)


