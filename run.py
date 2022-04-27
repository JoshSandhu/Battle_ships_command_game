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


def generate_ships_coord(board):
    """
    Generating 4 ships to be on the board.
    The while loop ensures all 4 are generated.
    Generating random co-ordinates the computer places a 
    "o", then simply countsd how many are on the board.
    The while loop finshes when the count is at 4.
    Argument: list
    """
    ship_amount = 0
    while ship_amount < 4:
        ship_amount = 0
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_row][ship_col] = " o "
        # Every list in the board we look for a " o " and keep running
        for row in board:
            ship_amount += row.count(" o ")


def welcome():
    """
    Welcome message for the game which also
    has an input for the player to submit their name
    """
    print('Welcome to a command line of the classic Battleships')
    name = input("Please enter your name followed by the enter button: \n")
    print(f'\n Hi there {name}!'
          'The system will generate the loactions for your ships.'
          'There will be 4 Battleships to find within the computers board')
    print('\n X are marked as empty locations,'
          ' * are missed shots and the # are hits'
          'The grid is 5 spaces and they use integers between 1 and 5')


