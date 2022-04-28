from random import randint

user = []
user_guess = []
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


def generate_boards():
    """
    This function will create all the boards needed.
    A user's board which will hide all the users ships.
    A comp board is the same for the computer.
    This will also hide the comp ships from user.
    """
    gen_board(user)
    gen_board(computer)
    gen_board(user_guess)
    generate_ships_coord(user)
    generate_ships_coord(computer)


def user_shot():
    """
    This is to receive the users turn.
    We will then confirm the data is valid.
    After confirming a hit or miss we print
    the result of the turn.
    """
    print("Computer's board:")
    print_board(user_guess)
    repeat = True
    while repeat:
        # This is used to validate the input of the choices.
        while True:
            print("\nPlease choose a column for your shot.")
            guess_col = input("Enter a number (1-5) then press Enter: \n")
            if validate_data(guess_col):
                break
        while True:
            print("\nPlease choose a row for your shot.")
            guess_row = input("Enter a number (1-5) then press Enter: \n")
            if validate_data(guess_row):
                break

        # Now we minus 1 from the users input.
        guess_col = int(guess_col) - 1
        guess_row = int(guess_row) - 1

        # Here we choose a response if the spot has already been chosen.
        if (user_guess[guess_col][guess_row] == " * " or
                user_guess[guess_col][guess_row] == " # "):
            print("Unfortunatly you have already chosen that spot, try again!")
        else:
            repeat = False
    
    # Now we check whether its a hit or not.
    if computer[guess_col][guess_row] == " o ":
        user_guess[guess_col][guess_row] = " # "
        print("\nBOOOOM!! You have hit the computers ship!")
    else:
        user_guess[guess_col][guess_row] = " * "
        print("\nAhhh you missed this turn. Try again next time :")


def comp_shot():
    """
    Now we do the same as above for the computers shot
    """
    print("\nNow it is the computers shot.")
    repeat = True
    # Random number generation
    guess_col = random_num(computer)
    guess_row = random_num(computer)
    # Check if the spot has been chosen
    while repeat:
        if (user[guess_col][guess_row] == " * " or
                user[guess_col][guess_row] == " # "):
            guess_col = random_num(computer)
            guess_row = random_num(computer)
        else:
            repeat = False
    # Show the user the computers move.
    print(f"The computer has chosen {guess_col + 1}, {guess_row + 1}")
    if user[guess_col][guess_row] == " o ":
        user[guess_col][guess_row] = " # "
        print("Ahhh that is a direct hit!")
    else:
        user[guess_col][guess_row] = " * "
        print("The computer has missed!!")

