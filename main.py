import math
import graphics

# Global variables
ALLOWED_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ALLOWED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def validate_turns(turns):
    '''
    Validate user input for number of turns
        @param string turns User input to be validated
        @return list [True, []] if valid, otherwise [False, [errors]]
    '''
    is_valid = False
    errors = []
    result = []

    if turns == 'exit' or turns == 'quit':
        graphics.print_outro()

    try:
        turns = int(turns)
    except ValueError:
        errors.append('Invalid format. Please enter a number between 1 and 1000.')
    except:
        errors.append('Unexpected error. Please try again or enter exit or quit if you want to finish the game.')
    else:
        if turns > 1000:
            errors.append('Maximum number of turns: 1000')
        elif turns < 1:
            errors.append('Minimum number of turns: 1')
        else:
            is_valid = True

    result.extend([is_valid, errors])
    return result


def turns_to_play():
    answer_turns = True
    while answer_turns:
        turns = input('\nHow many turns do you want to play: ')
        valid_user_input = validate_turns(turns)
        if valid_user_input[0]:
            answer_turns = False
        else:
            [print(error) for error in valid_user_input[1]]
    return turns


def init_board():
    '''
    Initialize the board
        @return list 10x10 grid as the initial board 
    '''
    board = []
    for x in range(10):
        board.append(['O'] * 10)
    return board


def create_allowed_coords():
    '''
    Creates a list with default values for the allowed coordinates, used in placement phase
        @return list List of list of x, y values
    '''
    coords = []
    return [[coords.append([i, j]) for j in range(10)] for i in range(10)]
    #for i in range(10):
    #    for j in range(10):
    #        coords.append([i, j])
    #return coords


def main():

    # Start Game
    graphics.print_intro()

    # Ask turn number and convert it to 2 players' turns
    turns = int(turns_to_play()) * 2

    # Create board for both players
    board_p1 = init_board()
    board_p2 = init_board()

    # Create allowed_coords list for both users
    allowed_coords_p1 = create_allowed_coords()
    allowed_coords_p2 = create_allowed_coords()

    # Players place ships
    print('\nPlayer 1 place your ships: ')
    ships_p1 = create_ships(1)

    print('\nPlayer 2 place your ships: ')
    ships_p2 = create_ships(2)

    print('\n')

    # Begin Turns
    for turn in range(turns):
        if turn % 2 == 0:       # player1
            print_board(board_p1)
            print('Turn', math.ceil((turn + 1) / 2))
            print('Hello Player 1!')
            # Ask user for a guess
            shootTo = []
            shootTo = user_guess()
            # Evaluate user guess
            if evaluate_guess(shootTo, board_p1, ships_p2):
                break
        else:                   # player2
            print_board(board_p2)
            print('Turn', math.ceil((turn + 1) / 2))
            print('Hello Player 2!')
            # Ask user for a guess
            shootTo = []
            shootTo = user_guess()
            # Evaluate user guess
            if evaluate_guess(shootTo, board_p2, ships_p1):
                break


if __name__ == '__main__':
    main()


'''
- init_board function modified --> board has become a local variable instead of global variable, change main accordingly
- graphics.print_outro() --> define more thoroughly
'''
