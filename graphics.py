
import colored
from colored import fg, bg, attr
from colored import stylize
from pyfiglet import Figlet

# Global variables
ALLOWED_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ALLOWED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_intro():
    '''
    Print welcome screen
        @return None
    '''
    print('\nBattleship Game\n')
    print(' __________         __    __  .__                .__    .__')
    print(' \______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____')
    print('  |    |  _/\__  \\   __\   __\   | _/ __ \ /  ___/  |  \|  \____ \ ')
    print('  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >')
    print('  |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ ')
    print('         \/      \/                     \/     \/     \/   |__|    ')
    print('\n')


def init_board():
    '''
    Initialize the board
        @return list 10x10 grid as the initial board
    '''
    board = []
    for x in range(10):
        board.append(['~'] * 10)
    return board


def print_board(board, player):
    '''
    Print the board
        @return None
    '''
    color_sea = fg('#C0C0C0') + bg('deep_sky_blue_4b')
    color_player = fg('white')
    res = attr('reset')
    print('\n')
    print(' '*5 + '   '.join([str(number) for number in ALLOWED_NUMBERS]), sep='')
    print(res + ' '*3 + color_sea + '╔' + ('═'*3 + '╦')*9 + '═'*3 + '╗' + res)
    for count, row in enumerate(board):
        print(res + ' ' + ALLOWED_LETTERS[count] + ' ' + color_sea + '║ ' + ' ║ '.join(row) + ' ║' + res)
        if count == 9:
            print(res + ' '*3 + color_sea + '╚' + ('═'*3 + '╩')*9 + '═'*3 + '╝' + res)
        else:
            print(res + ' '*3 + color_sea + '╠' + ('═'*3 + '╬')*9 + '═'*3 + '╣' + res)

    print(res + ' '*3 + color_player + '╔' + '═'*39 + '╗' + res)
    print(res + ' '*3 + color_player + '║' + (str(player) + "'s board").center(39) + '║' + res)
    print(res + ' '*3 + color_player + '╚' + '═'*39 + '╝' + res)


def player_turn_ascii(player):
    '''
    Print player specific ascii graphics
        @return void
    '''
    img = Figlet(font='big', direction='auto', justify='left')
    print(img.renderText("{}'s turn :".format(player)))
