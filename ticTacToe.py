#Ti-Tac-Toe of any Size (TTTS) by Matthew Bencomo
#CSE210, BYU Idaho, Fall 2022 Semester
from sys import exit


def main():
    '''
    Main program logic and game loop
    
    pramaters: none
    return: none
    '''
    print(f'\nWelcome to Tic-Tac-Toe! The only winning move is not playing.')
    # Try/except is used to validate user input, ensuring we catch if the user fails to imput an integer.
    while True:
        try:
            size = int(
                input(
                    '\nPlease enter the numer of rows to play.\nThree is normal, while other sizes are experimental: '
                ))
            if size < 3:
                print(
                    'You cannot play a game of Tic-Tac-Toe with less than 9 spaces silly! I warned you.'
                )
            # Set up the game state for the first turn
            game_board = create_board(size)
            player = get_player('')
            # Main Game Loop
            while is_draw(game_board) == False:
                # This if statements cuts the game off before the loser is able to input a move
                if is_game_over(game_board):
                    break
                draw_game_area(game_board)
                get_player_input(game_board, player)
                player = get_player(player)
            break
        except ValueError:
            print('That is not a valid game size!')


def create_board(size: int) -> dict:
    '''
    Creates a dictionary where each row is a key:value pair, where the number of keys equals 'size' 
    and the number of elements equals 'size'.
    
    parameters:
        size: the dimension of the board, for both rows and columns since it is a square
    return: reference to board dict
    '''
    board = {}
    row = []
    ROW_INDEX = 0
    for x in range(size**2):
        # Check if the number of value elements is equal to the number of rows
        if (x + 1) % size == 0:
            row.append(x)
            board[ROW_INDEX] = row
            row = []
            ROW_INDEX += 1
        else:
            row.append(x)
    return board


def draw_game_area(board: dict):
    '''
    Draw the game board, with fancy spacing characters.

    parameters:
        board: a dictionary that contains the game state
    return: none
    '''
    line = ''
    spacer = ''
    size = len(board)
    print()
    # Create the spacer line in between rows
    for x in range(size):
        if (x + 1) % size == 0:
            spacer += '----'
        else:
            spacer += '----+'
    print(spacer)
    # Create a string for each row and print it one at a time
    for x, y in board.items():
        row = board[x]
        for cell in range(size):
            if (cell + 1) % size == 0:
                line += f' {row[cell]:<2}'
            else:
                line += f' {row[cell]:<2} |'
            if (cell + 1) % size == 0:
                print(line)
                print(spacer)
                line = ''
    print()


def get_player(player: str = '') -> str:
    '''
    Returns the next player to make a move.
    
    parameters:
        player: the previous player, the default empty string results in 'x' starting first
    return: player string ('x' or 'o')
    '''
    if player == '' or player == 'o':
        return 'x'
    else:
        return 'o'


def get_player_input(board: dict, player) -> bool:
    '''
    Gets the player's input and stores it in the board. This function also
    allows the user to end the game by returning a bool when END is typed.

    parameters:
        board: a dictionary that contains the game state
        player: the current player, as a string
    return: bool (True)
    '''
    max = len(board)**2
    while True:
        try:
            loc = input(
                f"{player}'s turn, pick a number from 0 to {max}, or type END: "
            )
            if loc.upper() == 'END':
                print('\nSo long, and thanks for all the fish!')
                exit()  # sys.exit() used to end the program early
            elif int(loc) >= max:
                print('That space does not exist')
            else:
                for key, value in board.items():
                    if int(loc) in value:
                        row = board[key]
                        row[row.index(int(loc))] = player
            break
        except ValueError:
            print('Invalid entry, please try again')


def is_game_over(board: dict) -> bool:
    '''
    Checks the rows, then columns, then diagonal for a tic-tac-toe

    parameters:
        board: dictionary containing the game state
        player: the current player
    return: bool
    '''
    size = len(board)
    # Check rows
    for key in board.keys():
        row = board[key]
        if row.count(row[0]) == size:
            print(f'\nThat is the game! {row[0]} wins.')
            draw_game_area(board)
            return True
    # Check Columns
    for x in range(size):
        col = []
        for y in range(size):
            row = board[y]
            col.append(row[x])
        if col.count(col[0]) == size:
            print(f'That is the game! {col[0]} wins.')
            draw_game_area(board)
            return True
    # Create list that contains the indexes of the diagonal cells
    diagonal = []
    for x in range(size):
        diagonal.append((size + 1) * x)
    # Create a list that contains the current game state
    rows = []
    for key, value in board.items():
        temp = board[key]
        for x in range(size):
            rows.append(temp[x])
    # Check diagonal #1
    for value in diagonal:
        diagonal[diagonal.index(value)] = rows[value]
        if diagonal.count(diagonal[0]) == size:
            print(f'\nThat is the game! {diagonal[0]} wins.')
            draw_game_area(board)
            return True
    # Recreate the diagonal list with indexes for the second diagonal
    diagonal = []
    for x in range(size):
        diagonal.append((size - 1) * (x + 1))
    # Check diagonal #2
    for value in diagonal:
        diagonal[diagonal.index(value)] = rows[value]
        if diagonal.count(diagonal[0]) == size:
            print(f'\nThat is the game! {diagonal[0]} wins.')
            draw_game_area(board)
            return True
    # If we didn't return previously, the game is still going
    return False


def is_draw(board: dict) -> bool:
    '''
    Checks to make sure all the cells are filled, before declaring a draw.
    
    parameters:
        board: dictionary containing game state
    return: bool
    '''
    size = len(board)
    # Iterate through every ke:value pair and check if it has a player in it
    for key, value in board.items():
        row = board[key]
        for value in row:
            if value == 'x' or value == 'o':
                continue
            else:
                return False
    print(f"\nCat's game! No winners.")
    draw_game_area(board)
    return True


if __name__ == '__main__':
    main()