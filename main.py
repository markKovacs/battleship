
import vlc
import math
import time
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


def enter_name(player):
    '''
    Ask user for his name during the game
        @param player   int   player number, 1 or 2
        @return player_name Name chosen by the user
    '''
    try:
        player_name = input('Player {}, please enter your name: '.format(player))
    except:
        player_name = 'Player ' + player
    return player_name


def play_sound(sound_name, sleep_before=0, sleep_after=0):
    try:
        time.sleep(sleep_before)
        vlc.MediaPlayer(sound_name + ".wav").play()
        time.sleep(sleep_after)
    except:
        pass


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


import intro
import outro
import controller


def main():

    # Start Game
    intro.print_intro()

    # Player 1 and 2 name
    p1_name = enter_name(1)
    p2_name = enter_name(2)

    # Ask turn number and convert it to 2 players' turns
    turns = int(turns_to_play()) * 2

    # Create board for both players - used for tracking players' guesses
    board_p1 = graphics.init_board()
    board_p2 = graphics.init_board()

    # Players place ships
    print('\n{}, place your ships: '.format(p1_name))
    ships_p1 = controller.create_ships(p1_name)

    print('\n{}, place your ships: '.format(p2_name))
    ships_p2 = controller.create_ships(p2_name)

    print('\n')

    # Begin Turns
    for turn in range(turns):
        if turn % 2 == 0:   # player1
            graphics.player_turn_ascii(p1_name)
            graphics.print_board(board_p1, p2_name)
            print("Turn {} - Hello {}!".format(math.ceil((turn + 1) / 2), p1_name))

            shootTo = controller.user_guess()

            evaluate_shootTo = controller.evaluate_guess(shootTo, board_p1, ships_p2)
            board_p1 = evaluate_shootTo[1]
            graphics.print_board(board_p1, p2_name)
            time.sleep(1)

            if evaluate_shootTo[0]:
                winner = 1
                break

        else:   # player2
            graphics.player_turn_ascii(p2_name)
            graphics.print_board(board_p2, p1_name)
            print("Turn {} - Hello {}!".format(math.ceil((turn + 1) / 2), p2_name))

            shootTo = controller.user_guess()

            evaluate_shootTo = controller.evaluate_guess(shootTo, board_p2, ships_p1)
            board_p2 = evaluate_shootTo[1]
            graphics.print_board(board_p2, p1_name)
            time.sleep(1)

            if evaluate_shootTo[0]:
                graphics.print_board(board_p2, p1_name)
                winner = 2
                break

        # check game end
        if turn == turns - 1:
            break

    if winner == 1:
        print('Game over! {} won!'.format(p1_name))
    elif winner == 2:
        print('Game over! {} won!'.format(p2_name))
    else:
        print("Game over! It's a draw!")

    # play_sound("victory", sleep_after=8)
    outro.print_outro()


if __name__ == '__main__':
    main()
