
import vlc
import math
import time
import graphics
import controller
import intro
import outro

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
        outro.print_outro()

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


def main():

    # Start Game
    graphics.print_intro()

    # Player 1 and 2 name
    p1_name = 'Peter'
    p2_name = 'Mark'

    # Ask turn number and convert it to 2 players' turns
    turns = int(turns_to_play()) * 2

    # Create board for both players - used for tracking players' guesses
    board_p1 = graphics.init_board()
    board_p2 = graphics.init_board()

    # Players place ships
    print('\nPlayer 1 place your ships: ')
    ships_p1 = controller.create_ships()

    print('\nPlayer 2 place your ships: ')
    ships_p2 = controller.create_ships()

    print('\n')

    # Begin Turns
    for turn in range(turns):
        if turn % 2 == 0:   # player1

            graphics.print_board(board_p1, p1_name)
            print("Turn {} - Hello {}!".format(math.ceil((turn + 1) / 2), p1_name))

            shootTo = controller.user_guess()

            evaluate_shootTo = controller.evaluate_guess(shootTo, board_p1, ships_p2)

            if evaluate_shootTo[0]:
                board_p1 = evaluate_shootTo[1]
                graphics.print_board(board_p1, p1_name)
                winner = 1
                break
            else:
                board_p1 = evaluate_shootTo[1]
                graphics.print_board(board_p1, p1_name)
        else:   # player2
            graphics.print_board(board_p2, p2_name)
            print("Turn {} - Hello {}!".format(math.ceil((turn + 1) / 2), p2_name))
            # print('Turn', math.ceil((turn + 1) / 2))
            # print('Hello Player 2!')

            shootTo = controller.user_guess()

            evaluate_shootTo = controller.evaluate_guess(shootTo, board_p1, ships_p2)

            if evaluate_shootTo[0]:
                board_p2 = evaluate_shootTo[1]
                graphics.print_board(board_p2, p2_name)
                winner = 2
                break
            else:
                board_p2 = evaluate_shootTo[1]
                graphics.print_board(board_p2, p2_name)

        if turn == turns - 1:   # check game end
            winner = 3
            break

    if winner == 1:
        print('Game over! {} won!'.format(p1_name))
    elif winner == 2:
        print('Game over! {} won!'.format(p2_name))
    elif winner == 3:
        print("Game over! It's a draw!")

    outro.print_outro()


if __name__ == '__main__':
    main()
