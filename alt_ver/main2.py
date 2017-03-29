import math
import graphics
import controller
import art_int
"""
letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
inv_letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
allowed_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
allowed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

def main():

    # Create graphical board
    board_p1 = graphics.init_board()
    board_p2 = graphics.init_board()

    # Create allowed_coords list for both users
    allowed_coords_p1 = controller.create_allowed_coords()
    allowed_coords_p2 = controller.create_allowed_coords()

    # Start Game - Intro Screen
    graphics.print_intro()

    while True:
        try:
            turns = input('How many turns do you want to play: ')
            if turns == 'exit' or turns == 'quit':
                break
            turns = int(turns) * 2
            if turns > 10000:
                print('Maximum number of turns: 1000')
                raise ValueError
            elif turns < 1:
                print('Minimum number of turns: 1')
                raise ValueError
            break
        except ValueError:
            print('Please specify a number between 1-10000! (Enter exit or quit if you want to finish the game')
        except:
            print('\nAn error occured.')
        finally:
            if turns == 'exit' or turns == 'quit':
                exit()

    # Players place ships - example for coords: 11
    print('\n')
    print('Player 1 place your ships: ')

    ships_p1 = controller.create_ships(1, allowed_coords_p1)

    print('\n')
    print('Player 2 place your ships: ')

    ships_p2 = controller.create_ships(2, allowed_coords_p2)

    print('\n')


    # Begin Turns
    for turn in range(turns):
        
        if turn % 2 == 0:       # player1
            print("value of board_p1 from main", board_p1)
            graphics.print_board(board_p1)
            print('Turn', math.ceil((turn + 1) / 2))
            print('Hello Player 1!')
            # Ask user for a guess
            shootTo = []
            shootTo = controller.user_guess()
            # Evaluate user guess
            if controller.evaluate_guess(shootTo, board_p1, ships_p2):
                break
        else:                   # player2
            graphics.print_board(board_p2)
            print('Turn', math.ceil((turn + 1) / 2))
            print('Hello Player 2!')
            # Ask user for a guess
            shootTo = []
            shootTo = controller.user_guess()
            # Evaluate user guess
            if controller.evaluate_guess(shootTo, board_p2, ships_p1):
                break


if __name__ == '__main__':
    main()
